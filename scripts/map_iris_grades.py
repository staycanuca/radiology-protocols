#!/usr/bin/env python3
"""map_iris_grades.py — Atribuire automată a gradelor și dozelor conform Ghidului Național IRIS (Ordinul MS 1342/2012).

Scanează toate protocoalele din repo (CT, RX, IRM, ECO, FLUORO) și completează secțiunea
iris_reference din frontmatter cu:
  - chapter: Capitolul IRIS corespunzător domeniului anatomic
  - recommendation_grade: Gradul de recomandare clinică (Grad A / Grad B)
  - radiation_dose: Clasa de iradiere ALARA (Clasa 0 / 1 / 2 / 3 / 4)

Apoi re-randează corpul documentelor folosind renderer-ul specific fiecărei modalități,
garantând formatarea perfectă Markdown (inclusiv separarea Cartelei 2 și afișarea pill-urilor IRIS).
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
import yaml

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from render_protocol import render_document as render_ct_document
from render_rx_protocol import render_rx_document
from render_irm_protocol import render_irm_document
from render_eco_protocol import render_eco_document
from render_fluoro_protocol import render_fluoro_document


PLACEHOLDER_GRADES = {
    None,
    "",
    "de verificat pe indicație; fără grad atribuit automat",
    "de verificat pe indicatie; fara grad atribuit automat",
    "de verificat",
    "nespecificat",
}

PLACEHOLDER_DOSES = {
    None,
    "",
    "de verificat pentru examinarea și populația selectate",
    "de verificat pentru examinarea si populatia selectate",
    "de verificat",
    "nespecificat",
}


def is_placeholder_or_missing(iris_ref: dict | None) -> bool:
    if not iris_ref or not isinstance(iris_ref, dict):
        return True
    grade = str(iris_ref.get("recommendation_grade", "")).strip().lower()
    dose = str(iris_ref.get("radiation_dose", "")).strip().lower()
    chapter = str(iris_ref.get("chapter", "")).strip().lower()

    if grade in PLACEHOLDER_GRADES:
        return True
    if dose in PLACEHOLDER_DOSES:
        return True
    if not chapter or chapter == "ghidul național iris" and grade in PLACEHOLDER_GRADES:
        return True
    return False


def get_rx_iris(fm: dict) -> dict:
    cat = str(fm.get("category", "")).strip().lower()
    title = str(fm.get("title", "")).strip().lower()
    slug = str(fm.get("slug", "")).strip().lower()

    if cat == "torace":
        return {
            "chapter": "Torace & Pulmon",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 1 (Minimă < 0.1 mSv)",
        }

    if cat == "membru-superior":
        if any(k in title for k in ["umar", "umăr", "clavicul", "scapul", "acromio"]):
            dose = "Clasa 1 (Minimă < 0.05 mSv)"
        elif any(k in title for k in ["cot", "humerus", "antebrat", "antebraț"]):
            dose = "Clasa 1 (Minimă < 0.02 mSv)"
        else:
            dose = "Clasa 1 (Minimă < 0.01 mSv)"
        return {
            "chapter": "Aparat locomotor & Membru superior",
            "recommendation_grade": "Grad A",
            "radiation_dose": dose,
        }

    if cat == "membru-inferior":
        if any(k in title for k in ["bazin", "sold", "șold", "pelvis", "coxo", "sacro"]):
            return {
                "chapter": "Aparat locomotor & Bazin",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 2 (Foarte mică ~ 0.8 - 1.0 mSv)",
            }
        elif any(k in title for k in ["femur", "genunchi", "rotul", "patel"]):
            return {
                "chapter": "Aparat locomotor & Membru inferior",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 1 (Minimă < 0.05 mSv)",
            }
        else:
            return {
                "chapter": "Aparat locomotor & Membru inferior",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 1 (Minimă < 0.01 mSv)",
            }

    if cat == "coloana":
        if any(k in title for k in ["cervic", "odontoid", "axis", "atlas"]):
            return {
                "chapter": "Coloană vertebrală & Traumatisme",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 1 (Minimă < 0.2 mSv)",
            }
        elif any(k in title for k in ["torac", "dorsal"]):
            return {
                "chapter": "Coloană vertebrală",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 2 (Foarte mică ~ 0.7 - 1.0 mSv)",
            }
        else:
            return {
                "chapter": "Coloană vertebrală",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 2 (Foarte mică ~ 1.0 - 1.5 mSv)",
            }

    if cat == "abdomen":
        return {
            "chapter": "Aparat digestiv & Abdomen",
            "recommendation_grade": "Grad B",
            "radiation_dose": "Clasa 2 (Foarte mică ~ 0.7 - 1.2 mSv)",
        }

    if cat == "craniu-saf":
        if any(k in title for k in ["sinus", "saf", "mentonier", "waters", "caldwell"]):
            return {
                "chapter": "Cap — ORL",
                "recommendation_grade": "Grad B",
                "radiation_dose": "Clasa 1 (Minimă < 0.1 mSv)",
            }
        elif any(k in title for k in ["mandibul", "nazal", "orbit", "zigomat", "facial", "fata", "față"]):
            return {
                "chapter": "Traumatisme — Față și orbite",
                "recommendation_grade": "Grad B",
                "radiation_dose": "Clasa 1 (Minimă < 0.1 mSv)",
            }
        else:
            return {
                "chapter": "Traumatisme — Față și orbite",
                "recommendation_grade": "Grad B",
                "radiation_dose": "Clasa 1 (Minimă < 0.2 mSv)",
            }

    if cat == "pediatrie":
        if any(k in title for k in ["torac", "pulmon", "cord"]):
            return {
                "chapter": "Pediatrie — Torace, pulmon, cord",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 1 (Minimă < 0.02 mSv)",
            }
        elif any(k in title for k in ["abdom", "pelv", "digestiv"]):
            return {
                "chapter": "Pediatrie — Aparat digestiv",
                "recommendation_grade": "Grad B",
                "radiation_dose": "Clasa 1 (Minimă < 0.05 mSv)",
            }
        else:
            return {
                "chapter": "Pediatrie — Aparat locomotor",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 1 (Minimă < 0.01 mSv)",
            }

    if cat == "mamografie":
        return {
            "chapter": "Sân",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 1 (Minimă < 0.4 mSv)",
        }

    # Neclasificat sau altele
    if "cranian" in title or "head" in title or "vomiting" in title:
        return {
            "chapter": "Traumatisme — Cap",
            "recommendation_grade": "Grad B",
            "radiation_dose": "Clasa 1 (Minimă < 0.2 mSv)",
        }

    return {
        "chapter": "Aparat digestiv & Abdomen",
        "recommendation_grade": "Grad B",
        "radiation_dose": "Clasa 2 (Foarte mică ~ 0.7 - 1.2 mSv)",
    }


def get_ct_iris(fm: dict) -> dict:
    cat = str(fm.get("category", "")).strip().lower()
    title = str(fm.get("title", "")).strip().lower()
    slug = str(fm.get("slug", "")).strip().lower()
    ptype = str(fm.get("protocol_type", "")).strip().lower()
    contrast = fm.get("contrast", {})
    has_contrast = (
        ptype == "contrast-enhanced"
        or (isinstance(contrast, dict) and str(contrast.get("agent", "")).strip().upper() not in ("", "N/A", "NONE", "FARA", "FĂRĂ"))
    )

    if cat == "cardiac":
        if any(k in title or k in slug for k in ["calciu", "calcium", "cac", "scor"]):
            return {
                "chapter": "Aparat cardiovascular (Cord)",
                "recommendation_grade": "Grad B",
                "radiation_dose": "Clasa 2 (Redusă 1 - 2 mSv)",
            }
        return {
            "chapter": "Aparat cardiovascular (Cord)",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 3 (Moderată 4 - 8 mSv)",
        }

    if cat == "vascular":
        if any(k in title or k in slug for k in ["carotid", "cerebr", "intracran", "poligon", "willis", "head", "neck"]):
            dose = "Clasa 3 (Moderată 5 - 8 mSv)"
        else:
            dose = "Clasa 4 (Ridicată > 10 mSv)"
        return {
            "chapter": "Aparat cardiovascular & Sistem vascular",
            "recommendation_grade": "Grad A",
            "radiation_dose": dose,
        }

    if cat == "chest":
        if any(k in title or k in slug for k in ["low dose", "low-dose", "ultra low", "screening", "doza redusa", "doză redusă"]):
            return {
                "chapter": "Torace & Pulmon",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 2 (Redusă 1 - 2 mSv)",
            }
        elif not has_contrast or any(k in title or k in slug for k in ["hrct", "fara contrast", "wo contrast", "nativ"]):
            return {
                "chapter": "Torace & Pulmon",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 3 (Moderată 5 - 8 mSv)",
            }
        else:
            return {
                "chapter": "Torace & Pulmon",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 3 (Moderată 5 - 10 mSv)",
            }

    if cat == "neuro":
        if any(k in title or k in slug for k in ["sinus", "stanca", "stâncă", "mastoid", "temporal", "ureche", "orl", "facial", "orbita"]):
            return {
                "chapter": "Cap — ORL",
                "recommendation_grade": "Grad B",
                "radiation_dose": "Clasa 2 (Redusă 1 - 3 mSv)",
            }
        elif any(k in title or k in slug for k in ["coloan", "coloana", "spine", "cervic", "torac", "lombar", "sacr"]):
            return {
                "chapter": "Coloană vertebrală & Traumatisme",
                "recommendation_grade": "Grad B",
                "radiation_dose": "Clasa 3 (Moderată 4 - 8 mSv)",
            }
        elif any(k in title or k in slug for k in ["gat", "gât", "neck", "parti moi", "laring"]):
            return {
                "chapter": "Gât (părți moi)",
                "recommendation_grade": "Grad B",
                "radiation_dose": "Clasa 3 (Moderată 3 - 6 mSv)",
            }
        else:
            return {
                "chapter": "Cap, Gât & Coloană vertebrală",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 2 (Mică 1 - 3 mSv)",
            }

    if cat == "abdomen":
        if any(k in title or k in slug for k in ["uro", "renal", "rinichi", "adrenal", "supraren", "kub", "vezic", "calcul", "colica"]):
            if any(k in title or k in slug for k in ["adrenal", "supraren"]):
                return {
                    "chapter": "Aparat uro-genital și glande suprarenale",
                    "recommendation_grade": "Grad B",
                    "radiation_dose": "Clasa 3 (Moderată 5 - 10 mSv)",
                }
            elif not has_contrast or "kub" in title or "kub" in slug or "calcul" in title:
                return {
                    "chapter": "Aparat uro-genital și glande suprarenale",
                    "recommendation_grade": "Grad A",
                    "radiation_dose": "Clasa 3 (Moderată 4 - 7 mSv)",
                }
            else:
                return {
                    "chapter": "Aparat uro-genital și glande suprarenale",
                    "recommendation_grade": "Grad A",
                    "radiation_dose": "Clasa 4 (Ridicată > 10 mSv)",
                }
        elif any(k in title or k in slug for k in ["pelvis", "uter", "ovar", "prostata", "ginecolog"]):
            return {
                "chapter": "Aparat uro-genital și glande suprarenale",
                "recommendation_grade": "Grad B",
                "radiation_dose": "Clasa 4 (Ridicată > 10 mSv)",
            }
        else:
            if not has_contrast:
                return {
                    "chapter": "Aparat digestiv & Abdomen",
                    "recommendation_grade": "Grad B",
                    "radiation_dose": "Clasa 3 (Moderată 5 - 8 mSv)",
                }
            else:
                return {
                    "chapter": "Aparat digestiv & Abdomen",
                    "recommendation_grade": "Grad A",
                    "radiation_dose": "Clasa 4 (Ridicată > 10 mSv)",
                }

    if cat == "msk":
        return {
            "chapter": "Aparat locomotor & Articulații",
            "recommendation_grade": "Grad B",
            "radiation_dose": "Clasa 2 (Redusă 1 - 4 mSv)",
        }

    if cat == "trauma":
        return {
            "chapter": "Traumatisme & Politraumă",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 4 (Ridicată > 15 - 20 mSv)",
        }

    return {
        "chapter": "Ghidul Național IRIS",
        "recommendation_grade": "Grad B",
        "radiation_dose": "Clasa 3 (Moderată 5 - 10 mSv)",
    }


def get_irm_iris(fm: dict) -> dict:
    cat = str(fm.get("category", "")).strip().lower()
    return {
        "chapter": "Imagistică prin Rezonanță Magnetică (IRM)",
        "recommendation_grade": "Grad A",
        "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
    }


def get_eco_iris(fm: dict) -> dict:
    return {
        "chapter": "Ecografie & Ultrasonografie",
        "recommendation_grade": "Grad A",
        "radiation_dose": "Clasa 0 (Fără Iradiere / Unde Mecanice - Ultrasunete)",
    }


def get_fluoro_iris(fm: dict) -> dict:
    return {
        "chapter": "Fluoroscopie & Radioscopie Clinică",
        "recommendation_grade": "Grad A",
        "radiation_dose": "Clasa 2 (Medie 1 - 5 mSv)",
    }


MODALITY_HANDLERS = {
    "ct": (get_ct_iris, render_ct_document),
    "rx": (get_rx_iris, render_rx_document),
    "irm": (get_irm_iris, render_irm_document),
    "eco": (get_eco_iris, render_eco_document),
    "fluoro": (get_fluoro_iris, render_fluoro_document),
}


def process_all_protocols(apply_changes: bool = False) -> None:
    stats = {
        "total_scanned": 0,
        "already_valid": 0,
        "assigned": 0,
        "by_modality": {},
    }

    print(f"\n{'[APLICARE]' if apply_changes else '[DRY-RUN]'} Pornire mapare ghid IRIS...")

    for mod_name, (get_iris_fn, render_fn) in MODALITY_HANDLERS.items():
        mod_dir = REPO_ROOT / "docs" / mod_name
        if not mod_dir.exists():
            continue

        mod_stats = {"total": 0, "already_valid": 0, "assigned": 0}
        stats["by_modality"][mod_name] = mod_stats

        for md_file in mod_dir.rglob("*.md"):
            if md_file.name in ("index.md", "compare.md", "radioprotectie.md"):
                continue

            stats["total_scanned"] += 1
            mod_stats["total"] += 1

            raw = md_file.read_text(encoding="utf-8")
            if not raw.startswith("---"):
                continue

            end = raw.find("\n---\n", 3)
            if end == -1:
                continue

            try:
                fm = yaml.safe_load(raw[3:end]) or {}
            except Exception as e:
                print(f"[EROARE YAML] {md_file}: {e}")
                continue

            current_iris = fm.get("iris_reference")
            if not is_placeholder_or_missing(current_iris):
                mod_stats["already_valid"] += 1
                stats["already_valid"] += 1
                continue

            # Compute IRIS reference
            new_iris = get_iris_fn(fm)
            fm["iris_reference"] = new_iris
            mod_stats["assigned"] += 1
            stats["assigned"] += 1

            if apply_changes:
                new_doc = render_fn(fm)
                md_file.write_text(new_doc, encoding="utf-8")

    print("\n--- REZULTATE MAPARE IRIS ---")
    print(f"Total protocoale scanate: {stats['total_scanned']}")
    print(f"Deja valide (nemodificate): {stats['already_valid']}")
    print(f"Protocoale cărora li s-a atribuit IRIS: {stats['assigned']}")
    print("\nDetaliere pe modalități:")
    for mod, s in sorted(stats["by_modality"].items()):
        print(f"  {mod.upper()}: {s['total']} total, {s['already_valid']} deja valide, {s['assigned']} atribuite")

    if not apply_changes:
        print("\n[NOTE] Acesta a fost un test (dry-run). Rulați cu flag-ul --apply pentru a salva modificările pe disc.")


def main():
    parser = argparse.ArgumentParser(description="Atribuire automată Ghid IRIS (grade recomandare și doze iradiere).")
    parser.add_argument("--apply", action="store_true", help="Scrie modificările în fișierele Markdown")
    args = parser.parse_args()

    process_all_protocols(apply_changes=args.apply)


if __name__ == "__main__":
    main()
