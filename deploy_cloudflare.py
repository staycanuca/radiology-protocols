#!/usr/bin/env python3
"""deploy_cloudflare.py — Script automatizat de deploy pe Cloudflare Pages pentru proiectul 'protocoale'.

Funcționalitate:
1. Verifică existența și integritatea folderului static 'site/'.
2. Oferă opțiunea de compilare/re-compilare automată a site-ului dacă este necesar sau la cerere (--build).
3. Verifică disponibilitatea uneltelor Node.js / npx.
4. Execută comanda oficială Cloudflare Wrangler:
   npx wrangler pages deploy site --project-name=protocoale

Utilizare:
    python deploy_cloudflare.py          -> Verifică și face deploy direct la folderul 'site/'
    python deploy_cloudflare.py --build  -> Reconstruiește mai întâi site-ul static și apoi face deploy
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

# Suport UTF-8 pentru terminalele Windows
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if sys.stderr and hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parent
SITE_DIR = REPO_ROOT / "site"
PROJECT_NAME = "protocoale"

class Colors:
    CYAN = "\033[96m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RESET = "\033[0m"


def print_banner():
    print(f"""
{Colors.CYAN}{Colors.BOLD}╔════════════════════════════════════════════════════════════════════════════╗
║                  DEPLOY AUTOMATIZAT PE CLOUDFLARE PAGES                    ║
╠════════════════════════════════════════════════════════════════════════════╣
║  Proiect Cloudflare:  {Colors.GREEN}{Colors.BOLD}{PROJECT_NAME:<44}{Colors.RESET}{Colors.CYAN}{Colors.BOLD}║
║  Folder sursă:        {Colors.BLUE}{Colors.BOLD}{str(SITE_DIR.name) + '/':<44}{Colors.RESET}{Colors.CYAN}{Colors.BOLD}║
╚════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
""")


def check_node_npx() -> bool:
    """Verifică dacă npx este instalat și disponibil în PATH."""
    npx_path = shutil.which("npx") or shutil.which("npx.cmd")
    if not npx_path:
        print(f"{Colors.RED}[✕] 'npx' nu a fost găsit în PATH!{Colors.RESET}")
        print("    Vă rugăm să instalați Node.js de la https://nodejs.org/")
        return False
    return True


def build_site() -> bool:
    """Rulează compilarea statică a site-ului (python run.py --build)."""
    print(f"{Colors.BLUE}{Colors.BOLD}>>> 1. Compilare site static (python run.py --build)...{Colors.RESET}")
    run_py = REPO_ROOT / "run.py"
    if run_py.exists():
        cmd = [sys.executable, str(run_py), "--build"]
    else:
        cmd = [sys.executable, "-m", "mkdocs", "build"]
        
    res = subprocess.run(cmd, cwd=str(REPO_ROOT))
    if res.returncode != 0:
        print(f"{Colors.RED}[✕] Compilarea site-ului a eșuat!{Colors.RESET}")
        return False
    print(f"{Colors.GREEN}✔ Compilare finalizată cu succes.{Colors.RESET}\n")
    return True


def check_site_dir(auto_build: bool = False) -> bool:
    """Verifică dacă folderul 'site/' există și conține fișiere."""
    if not SITE_DIR.exists() or not any(SITE_DIR.iterdir()):
        print(f"{Colors.YELLOW}[!] Folderul '{SITE_DIR.name}' nu există sau este gol.{Colors.RESET}")
        print("    Se pornește compilarea automată...")
        return build_site()
    
    html_count = len(list(SITE_DIR.rglob("*.html")))
    if html_count < 100:
        print(f"{Colors.YELLOW}[!] Folderul '{SITE_DIR.name}' conține doar {html_count} pagini HTML.{Colors.RESET}")
        if auto_build:
            return build_site()
    else:
        print(f"{Colors.GREEN}✔ Folderul '{SITE_DIR.name}' este pregătit ({html_count} pagini HTML găsite).{Colors.RESET}")
    return True


def deploy_to_cloudflare() -> int:
    """Execută comanda de deploy prin Wrangler."""
    print(f"\n{Colors.BLUE}{Colors.BOLD}>>> 2. Publicare pe Cloudflare Pages (wrangler pages deploy)...{Colors.RESET}")
    print(f"{Colors.DIM}Comandă: npx wrangler pages deploy site --project-name={PROJECT_NAME}{Colors.RESET}\n")
    
    # npx wrangler pages deploy site --project-name=protocoale
    cmd = [
        "npx",
        "wrangler",
        "pages",
        "deploy",
        "site",
        f"--project-name={PROJECT_NAME}",
        "--commit-dirty=true"
    ]
    
    # Pe Windows, apelurile către fișiere .cmd necesită shell=True dacă se rulează comanda ca string sau direct prin npx.cmd
    use_shell = sys.platform == "win32"
    
    start_time = time.time()
    try:
        res = subprocess.run(cmd, cwd=str(REPO_ROOT), shell=use_shell)
        elapsed = time.time() - start_time
        
        if res.returncode == 0:
            print(f"\n{Colors.GREEN}{Colors.BOLD}✔ DEPLOY FINALIZAT CU SUCCES în {elapsed:.1f}s!{Colors.RESET}")
            print(f"{Colors.CYAN}🌐 Site-ul dvs. este live la: {Colors.BOLD}https://{PROJECT_NAME}.pages.dev{Colors.RESET}\n")
            return 0
        else:
            print(f"\n{Colors.RED}[✕] Comanda de deploy a returnat codul de eroare {res.returncode}.{Colors.RESET}")
            print("    Dacă este prima dată când folosiți Wrangler, asigurați-vă că sunteți autentificat:")
            print("    Rulează în consolă: npx wrangler login")
            return res.returncode
    except Exception as e:
        print(f"\n{Colors.RED}[✕] Eroare la rularea comenzii wrangler: {e}{Colors.RESET}")
        return 1


def main():
    parser = argparse.ArgumentParser(description="Deploy site pe Cloudflare Pages (proiect: protocoale)")
    parser.add_argument("--build", action="store_true", help="Recompilează site-ul înainte de deploy")
    args = parser.parse_args()

    print_banner()

    if not check_node_npx():
        sys.exit(1)

    if args.build:
        if not build_site():
            sys.exit(1)
    else:
        if not check_site_dir(auto_build=True):
            sys.exit(1)

    code = deploy_to_cloudflare()
    sys.exit(code)


if __name__ == "__main__":
    main()
