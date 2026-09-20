#!/usr/bin/env python3
"""build_optimizer.py — Optimizare și compresie pentru HTML și imagini la build.

Funcționalitate:
1. Minificare HTML ultra-rapidă (folosind minify_html / Rust core, cu fallback regex).
2. Optimizare PNG și JPEG in-place (fără a schimba numele, extensia sau link-urile).
3. Execuție paralelă multi-threaded pentru viteză maximă.
4. Funcționează atât ca hook MkDocs (on_post_build), cât și rulat direct din CLI / run.py.
"""

from __future__ import annotations

import concurrent.futures
import io
import os
import re
import sys
import time
from pathlib import Path

# Suport UTF-8 pe terminalele Windows
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if sys.stderr and hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

try:
    import minify_html
    HAS_MINIFY_HTML = True
except ImportError:
    HAS_MINIFY_HTML = False

try:
    from PIL import Image
    HAS_PILLOW = True
except ImportError:
    HAS_PILLOW = False


def _minify_html_content(raw_html: str) -> str:
    """Minifică conținutul unui fișier HTML."""
    if HAS_MINIFY_HTML:
        try:
            return minify_html.minify(
                raw_html,
                minify_js=True,
                minify_css=True,
                keep_comments=False,
            )
        except Exception:
            pass

    # Fallback sigur bazat pe regex
    clean = re.sub(r'<!--(?!\s*\[if).*?-->', '', raw_html, flags=re.S)
    clean = re.sub(r'>\s+<', '><', clean)
    return clean


def _optimize_html_file(file_path: Path) -> tuple[int, int]:
    """Optimizează un singur fișier HTML. Returnează (dimensiune_initiala, dimensiune_finala)."""
    try:
        raw = file_path.read_text(encoding="utf-8", errors="ignore")
        orig_size = len(raw.encode("utf-8"))
        minified = _minify_html_content(raw)
        new_size = len(minified.encode("utf-8"))
        if new_size < orig_size:
            file_path.write_text(minified, encoding="utf-8")
            return orig_size, new_size
        return orig_size, orig_size
    except Exception:
        sz = file_path.stat().st_size
        return sz, sz


def _optimize_image_file(file_path: Path) -> tuple[int, int]:
    """Optimizează o imagine PNG/JPEG in-place. Returnează (dimensiune_initiala, dimensiune_finala)."""
    if not HAS_PILLOW:
        sz = file_path.stat().st_size
        return sz, sz

    suffix = file_path.suffix.lower()
    orig_size = file_path.stat().st_size

    try:
        with Image.open(file_path) as im:
            buf = io.BytesIO()
            if suffix == ".png":
                # Salvează PNG optimizat
                im.save(buf, format="PNG", optimize=True)
            elif suffix in (".jpg", ".jpeg"):
                # Salvează JPEG optimizat
                im.save(buf, format="JPEG", optimize=True, progressive=True, quality=im.quality if hasattr(im, "quality") else 85)
            else:
                return orig_size, orig_size

            new_size = buf.tell()
            if new_size < orig_size:
                file_path.write_bytes(buf.getvalue())
                return orig_size, new_size
            return orig_size, orig_size
    except Exception:
        return orig_size, orig_size


def optimize_site(site_dir: Path | str) -> dict:
    """Optimizează recursiv toate fișierele HTML și imaginile dintr-un director de site compilat."""
    site_path = Path(site_dir).resolve()
    if not site_path.is_dir():
        print(f"[build_optimizer] Directorul {site_path} nu există.")
        return {}

    start_time = time.time()
    print(f"\n[build_optimizer] 🚀 Pornire optimizare și compresie pentru: {site_path.name}/")

    # 1. Colectare fișiere
    html_files = list(site_path.rglob("*.html"))
    img_files = [f for f in site_path.rglob("*") if f.suffix.lower() in (".png", ".jpg", ".jpeg")]

    html_orig_total = 0
    html_opt_total = 0
    img_orig_total = 0
    img_opt_total = 0

    # 2. Minificare HTML în paralel
    if html_files:
        print(f"  • Minificare {len(html_files)} fișiere HTML...")
        with concurrent.futures.ThreadPoolExecutor(max_workers=min(16, (os.cpu_count() or 4) * 2)) as executor:
            results = executor.map(_optimize_html_file, html_files)
            for orig_sz, new_sz in results:
                html_orig_total += orig_sz
                html_opt_total += new_sz

    # 3. Optimizare imagini în paralel
    if img_files:
        print(f"  • Optimizare {len(img_files)} imagini (PNG & JPEG)...")
        with concurrent.futures.ThreadPoolExecutor(max_workers=min(8, os.cpu_count() or 4)) as executor:
            results = executor.map(_optimize_image_file, img_files)
            for orig_sz, new_sz in results:
                img_orig_total += orig_sz
                img_opt_total += new_sz

    duration = time.time() - start_time
    total_orig = html_orig_total + img_orig_total
    total_opt = html_opt_total + img_opt_total
    saved_bytes = total_orig - total_opt
    saved_mb = saved_bytes / (1024 * 1024)

    html_saved_mb = (html_orig_total - html_opt_total) / (1024 * 1024)
    img_saved_mb = (img_orig_total - img_opt_total) / (1024 * 1024)

    print(f"[build_optimizer] ✔ Optimizare finalizată în {duration:.2f}s!")
    print(f"    - HTML:    {html_orig_total / (1024*1024):.1f} MB -> {html_opt_total / (1024*1024):.1f} MB (-{html_saved_mb:.1f} MB)")
    print(f"    - Imagini: {img_orig_total / (1024*1024):.1f} MB -> {img_opt_total / (1024*1024):.1f} MB (-{img_saved_mb:.1f} MB)")
    print(f"    - TOTAL ECONOMISIT: {saved_mb:.1f} MB (reducere {((saved_bytes / total_orig) * 100 if total_orig else 0):.1f}%)\n")

    return {
        "duration_seconds": duration,
        "saved_mb": saved_mb,
        "html_saved_mb": html_saved_mb,
        "img_saved_mb": img_saved_mb,
    }


def on_post_build(config: dict) -> None:
    """MkDocs hook entrypoint: apelat automat la finalizarea comenzii 'mkdocs build'."""
    site_dir = config.get("site_dir", "site")
    # În modul 'serve' (dezvoltare), sărim optimizarea pentru viteză maximă de pornire și reîncărcare
    if any(arg in sys.argv for arg in ["serve", "--watch"]) or "mkdocs_" in str(site_dir):
        return
    optimize_site(site_dir)


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parents[1] / "site"
    optimize_site(target)
