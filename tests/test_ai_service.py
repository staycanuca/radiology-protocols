"""test_ai_service.py — Teste automate pentru serviciul AI și autentificare."""

import json
import os
import sys
from pathlib import Path

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from admin import app
from ai_service import generate_local_clinical_reply, search_clinical_context


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_search_clinical_context_iris():
    """Căutarea clinică trebuie să returneze situații relevante din Ghidul IRIS."""
    ctx = search_clinical_context("apendicită")
    assert "iris" in ctx
    assert len(ctx["iris"]) > 0
    # Verifică structura situației
    sit = ctx["iris"][0]
    assert "situation" in sit
    assert "recommendations" in sit


def test_search_clinical_context_protocols():
    """Căutarea clinică trebuie să identifice protocoale CT corelate."""
    ctx = search_clinical_context("embolie pulmonară")
    assert "protocols" in ctx
    titles = [p["title"].lower() for p in ctx["protocols"]]
    # Ar trebui să găsească PE sau pulmonar
    assert any("pe" in t or "pulmonar" in t or "embolism" in t for t in titles)


def test_search_clinical_context_rx():
    """Căutarea clinică trebuie să identifice protocoale Rx de radiografie convențională."""
    ctx = search_clinical_context("radiografie torace pneumonie")
    assert "rx" in ctx
    assert len(ctx["rx"]) > 0
    titles = [p["title"].lower() for p in ctx["rx"]]
    assert any("torace" in t for t in titles)


def test_local_clinical_reply_generation():
    """Generatorul local de răspuns trebuie să producă un text medical structurat."""
    ctx = search_clinical_context("cefalee")
    reply = generate_local_clinical_reply("cefalee", ctx)
    assert "Ghid Național IRIS" in reply
    assert "Ordinul MS nr. 1342/2012" in reply


def test_auth_status_endpoint(client):
    """Endpoint-ul /api/ai/auth/status trebuie să returneze JSON valid cu providers."""
    resp = client.get("/api/ai/auth/status")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["ok"] is True
    assert "providers" in data
    assert "gemini" in data["providers"]
    assert "openai" in data["providers"]


def test_auth_quick_endpoint(client):
    """Autentificarea clinică rapidă trebuie să creeze o sesiune validă."""
    resp = client.post("/api/ai/auth/quick", json={"name": "Dr. Popescu", "role": "Medic Radiolog"})
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["ok"] is True
    assert data["user"]["name"] == "Dr. Popescu"
    assert data["user"]["role"] == "Medic Radiolog"


def test_chat_endpoint_fallback(client):
    """Endpoint-ul de chat trebuie să răspundă chiar și pe fallback local fără cheie externă."""
    resp = client.post("/api/ai/chat", json={
        "message": "Ce investigație recomandați pentru apendicită suspectată?",
        "provider": "gemini",
        "mode": "all"
    })
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["ok"] is True
    assert "reply" in data
    assert len(data["reply"]) > 50
    assert "engine" in data


def test_anatomical_anchoring_cranial_trauma():
    """Optimizarea 1 & 3: Căutarea pentru traumatism cranian nu trebuie să aducă traumatisme abdominale sau protocoale periferice."""
    ctx = search_clinical_context("ce se recomanda pentru traumatism cranian?")
    sit_names = [s["situation"].lower() for s in ctx["iris"]]
    # Asigură că toate situațiile returnate țin de sfera craniană/neuro
    for name in sit_names:
        assert not any(w in name for w in ["hepatic", "splenic", "renal", "bazin", "abdomen"])
        assert any(w in name for w in ["cran", "cerebr", "inconstient"])

    # Protocoalele CT trebuie să fie strict craniu/coloană cervicală, nu membre sau abdomen
    ct_titles = [p["title"].lower() for p in ctx["protocols"]]
    for title in ct_titles:
        assert not any(w in title for w in ["membre", "femur", "gravida", "abdomen"])
        assert any(w in title for w in ["craniu", "cervical", "cerebral"])

    # Protocoalele Rx trebuie să fie coloană cervicală sau masiv facial, NU bazin sau torace
    rx_titles = [p["title"].lower() for p in ctx["rx"]]
    for title in rx_titles:
        assert "bazin" not in title
        assert "torace" not in title


def test_deduplication_in_iris_recommendations():
    """Optimizarea 2: Recomandările fiecărei situații IRIS trebuie să fie strict unice."""
    ctx = search_clinical_context("ce se recomanda pentru traumatism cranian?")
    for s in ctx["iris"]:
        seen_keys = set()
        for r in s["recommendations"]:
            key = (r.get("exam", "").lower().strip(), r.get("indication", "").lower().strip())
            assert key not in seen_keys, f"Duplicat găsit în {s['situation']}: {key}"
            seen_keys.add(key)


def test_search_clinical_context_irm():
    """Căutarea clinică trebuie să identifice protocoale IRM."""
    ctx = search_clinical_context("irm genunchi menisc")
    assert "irm" in ctx
    assert len(ctx["irm"]) > 0
    titles = [p["title"].lower() for p in ctx["irm"]]
    assert any("genunchi" in t for t in titles)


def test_local_clinical_reply_with_irm():
    """Generatorul local include secțiunea IRM când sunt găsite protocoale de Rezonanță Magnetică."""
    ctx = search_clinical_context("irm cerebral scleroza multipla")
    reply = generate_local_clinical_reply("irm cerebral scleroza multipla", ctx)
    assert "Protocoale Rezonanță Magnetică (IRM)" in reply
    assert "cerebral" in reply.lower()


def test_search_clinical_context_eco():
    """Căutarea clinică trebuie să identifice protocoale de Ecografie (US)."""
    ctx = search_clinical_context("ecografie tiroida nodul tirads")
    assert "eco" in ctx
    assert len(ctx["eco"]) > 0
    titles = [p["title"].lower() for p in ctx["eco"]]
    assert any("tiroid" in t for t in titles)


def test_local_clinical_reply_with_eco():
    """Generatorul local include secțiunea Ecografie când sunt găsite protocoale US."""
    ctx = search_clinical_context("ecografie fast trauma abdominala")
    reply = generate_local_clinical_reply("ecografie fast trauma abdominala", ctx)
    assert "Protocoale Ecografie & Ultrasonografie (US)" in reply
    assert "fast" in reply.lower() or "abdomen" in reply.lower()


def test_chat_endpoint_eco_context(client):
    """Endpoint-ul de chat include eco_count în context_matches."""
    resp = client.post("/api/ai/chat", json={
        "message": "Ce transductor se folosește la ecografie carotidiană doppler?",
        "provider": "gemini",
        "mode": "all"
    })
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["ok"] is True
    assert "eco_count" in data["context_matches"]
    assert data["context_matches"]["eco_count"] > 0



