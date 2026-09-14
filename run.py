#!/usr/bin/env python3
"""run.py — Launcher unitar și logic pentru Ghidul Protocoalelor de Radiologie.

Utilizare:
    python run.py             -> Deschide meniul interactiv
    python run.py --all       -> Pornește ambele servere (Ghid Protocoale + Panou Admin)
    python run.py --docs      -> Pornește doar Ghidul Protocoalelor (MkDocs pe port 8000)
    python run.py --admin     -> Pornește doar Panoul de Administrare (pe port 5173)
    python run.py --index     -> Re-generează toți indecșii (comparison, sitemap, forms)
    python run.py --test      -> Rulează suita de teste automate (pytest)
    python run.py --build     -> Construiește site-ul static pentru producție (site/)
"""

from __future__ import annotations

import argparse
import os
import shutil
import signal
import subprocess
import sys
import time
import webbrowser
from pathlib import Path

# Asigură codarea UTF-8 pe terminalele Windows
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if sys.stderr and hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).parent.resolve()
SCRIPTS_DIR = REPO_ROOT / "scripts"
DOCS_PORT = 8000
ADMIN_PORT = 5173

DOCS_URL = f"http://localhost:{DOCS_PORT}/radiology-protocols/"
ADMIN_URL = f"http://localhost:{ADMIN_PORT}"


# ---------------------------------------------------------------------------
# Culori și stilizare consolă
# ---------------------------------------------------------------------------

class Colors:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RESET = "\033[0m"


def print_banner():
    banner = f"""
{Colors.CYAN}{Colors.BOLD}╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║         GHIDUL PROTOCOALELOR DE RADIOLOGIE — LAUNCHER UNITAR               ║
║                     Departamentul de Radiologie                            ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(banner)


# ---------------------------------------------------------------------------
# Verificare cerințe și dependințe
# ---------------------------------------------------------------------------

REQUIRED_PACKAGES = {
    "mkdocs": "mkdocs",
    "material": "mkdocs-material",
    "mkdocs_awesome_pages_plugin": "mkdocs-awesome-pages-plugin",
    "flask": "flask",
    "yaml": "pyyaml",
    "pytest": "pytest",
}


def check_dependencies() -> bool:
    """Verifică dacă toate pachetele necesare sunt instalate."""
    missing = []
    for module_name, pip_name in REQUIRED_PACKAGES.items():
        try:
            __import__(module_name)
        except ImportError:
            missing.append(pip_name)

    if missing:
        print(f"\n{Colors.YELLOW}[!] Următoarele pachete lipsesc: {', '.join(missing)}{Colors.RESET}")
        resp = input(f"{Colors.BOLD}Doriți să le instalați automat acum? (d/n): {Colors.RESET}").strip().lower()
        if resp in ("d", "da", "y", "yes"):
            cmd = [sys.executable, "-m", "pip", "install", *missing]
            print(f"{Colors.DIM}Rulare: {' '.join(cmd)}{Colors.RESET}")
            res = subprocess.run(cmd)
            return res.returncode == 0
        return False
    return True


# ---------------------------------------------------------------------------
# Operațiuni de sistem
# ---------------------------------------------------------------------------

def run_indexes() -> bool:
    """Re-generează toți indecșii aplicației."""
    print(f"\n{Colors.BLUE}{Colors.BOLD}>>> Actualizare și re-generare indici...{Colors.RESET}")
    scripts = [
        ("generate_comparison_index.py", "Index comparare protocoale"),
        ("generate_sitemap.py", "Sitemap protocoale"),
        ("generate_forms_index.py", "Index formulare & config instituție"),
    ]
    all_ok = True
    for script_name, description in scripts:
        script_path = SCRIPTS_DIR / script_name
        if not script_path.exists():
            print(f"  {Colors.RED}[✕]{Colors.RESET} Scriptul {script_name} nu a fost găsit!")
            all_ok = False
            continue

        print(f"  {Colors.DIM}• Se generează {description} ({script_name})...{Colors.RESET}", end=" ", flush=True)
        res = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
        )
        if res.returncode == 0:
            print(f"{Colors.GREEN}[OK]{Colors.RESET}")
        else:
            print(f"{Colors.RED}[EROARE]{Colors.RESET}")
            if res.stderr:
                print(f"    {Colors.RED}{res.stderr.strip()}{Colors.RESET}")
            all_ok = False

    if all_ok:
        print(f"{Colors.GREEN}✔ Toți indecșii au fost actualizați cu succes.{Colors.RESET}")
    return all_ok


def run_tests() -> int:
    """Rulează suita de teste automate cu pytest."""
    print(f"\n{Colors.BLUE}{Colors.BOLD}>>> Rulare teste automate (pytest)...{Colors.RESET}\n")
    cmd = [sys.executable, "-m", "pytest", "-v"]
    res = subprocess.run(cmd, cwd=str(REPO_ROOT))
    return res.returncode


def run_build() -> int:
    """Construiește site-ul static pentru producție în directorul site/."""
    if not run_indexes():
        print(f"{Colors.YELLOW}[!] Avertisment: unii indici nu au putut fi generați înainte de build.{Colors.RESET}")
    print(f"\n{Colors.BLUE}{Colors.BOLD}>>> Construire site static (mkdocs build)...{Colors.RESET}\n")
    cmd = [sys.executable, "-m", "mkdocs", "build"]
    res = subprocess.run(cmd, cwd=str(REPO_ROOT))
    if res.returncode == 0:
        site_dir = REPO_ROOT / "site"
        print(f"\n{Colors.GREEN}✔ Site-ul a fost compilat cu succes în: {site_dir}{Colors.RESET}")
    return res.returncode


# ---------------------------------------------------------------------------
# Managementul serverelor (Docs & Admin)
# ---------------------------------------------------------------------------

def stop_process(proc: subprocess.Popen | None, name: str = "Proces"):
    """Oprește un proces în mod curat."""
    if proc is None or proc.poll() is not None:
        return
    try:
        proc.terminate()
        proc.wait(timeout=3)
    except Exception:
        try:
            proc.kill()
        except Exception:
            pass


def run_docs(open_browser: bool = True):
    """Rulează serverul MkDocs pe portul 8000."""
    run_indexes()
    print(f"\n{Colors.GREEN}{Colors.BOLD}>>> Pornire Ghid Protocoale (MkDocs) la {DOCS_URL}...{Colors.RESET}")
    print(f"{Colors.DIM}Apăsați Ctrl+C pentru a opri serverul.{Colors.RESET}\n")

    if open_browser:
        import threading
        threading.Timer(1.5, lambda: webbrowser.open(DOCS_URL)).start()

    cmd = [sys.executable, "-m", "mkdocs", "serve", "--watch", "docs", "--dev-addr", f"127.0.0.1:{DOCS_PORT}"]
    try:
        subprocess.run(cmd, cwd=str(REPO_ROOT))
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Serverul Ghid Protocoale a fost oprit.{Colors.RESET}")


def run_admin(open_browser: bool = True):
    """Rulează serverul Panoului de Administrare Flask pe portul 5173."""
    run_indexes()
    print(f"\n{Colors.GREEN}{Colors.BOLD}>>> Pornire Panou de Administrare la {ADMIN_URL}...{Colors.RESET}")
    print(f"{Colors.DIM}Apăsați Ctrl+C pentru a opri serverul.{Colors.RESET}\n")

    if open_browser:
        import threading
        threading.Timer(1.2, lambda: webbrowser.open(ADMIN_URL)).start()

    cmd = [sys.executable, str(SCRIPTS_DIR / "admin.py")]
    try:
        subprocess.run(cmd, cwd=str(REPO_ROOT))
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Panoul de Administrare a fost oprit.{Colors.RESET}")


def run_all(open_browser: bool = True):
    """Rulează ambele servere în paralel (Ghid Protocoale + Panou Administrare)."""
    run_indexes()

    print(f"\n{Colors.CYAN}{Colors.BOLD}╔════════════════════════════════════════════════════════════════════════════╗")
    print(f"║               SE PORNEȘTE MEDIUL COMPLET RADIOLOGY PROTOCOLS               ║")
    print(f"╠════════════════════════════════════════════════════════════════════════════╣")
    print(f"║  1. Ghid Protocoale (MkDocs):     {Colors.GREEN}{Colors.BOLD}{DOCS_URL:<40}{Colors.RESET}{Colors.CYAN}{Colors.BOLD}║")
    print(f"║  2. Panou Administrare (Admin):   {Colors.BLUE}{Colors.BOLD}{ADMIN_URL:<40}{Colors.RESET}{Colors.CYAN}{Colors.BOLD}║")
    print(f"╠════════════════════════════════════════════════════════════════════════════╣")
    print(f"║  {Colors.YELLOW}Apăsați Ctrl+C în orice moment pentru a opri ambele servere.{Colors.CYAN}{Colors.BOLD}              ║")
    print(f"╚════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")

    # Pornire MkDocs ca proces copil
    docs_cmd = [sys.executable, "-m", "mkdocs", "serve", "--watch", "docs", "--dev-addr", f"127.0.0.1:{DOCS_PORT}"]
    docs_proc = subprocess.Popen(docs_cmd, cwd=str(REPO_ROOT))

    # Pornire Admin Flask ca proces copil
    admin_cmd = [sys.executable, str(SCRIPTS_DIR / "admin.py")]
    admin_proc = subprocess.Popen(admin_cmd, cwd=str(REPO_ROOT))

    if open_browser:
        import threading
        threading.Timer(2.0, lambda: webbrowser.open(DOCS_URL)).start()
        threading.Timer(2.5, lambda: webbrowser.open(ADMIN_URL)).start()

    try:
        # Așteaptă până când oricare dintre procese se încheie sau utilizatorul apasă Ctrl+C
        while True:
            time.sleep(0.5)
            if docs_proc.poll() is not None:
                print(f"{Colors.YELLOW}[!] Serverul Ghid Protocoale s-a oprit neașteptat.{Colors.RESET}")
                break
            if admin_proc.poll() is not None:
                print(f"{Colors.YELLOW}[!] Serverul Panou Administrare s-a oprit neașteptat.{Colors.RESET}")
                break
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Oprire servere în curs...{Colors.RESET}")
    finally:
        stop_process(docs_proc, "Ghid Protocoale")
        stop_process(admin_proc, "Panou Administrare")
        print(f"{Colors.GREEN}✔ Toate serverele au fost oprite curat.{Colors.RESET}")


# ---------------------------------------------------------------------------
# Meniu Interactiv
# ---------------------------------------------------------------------------

def interactive_menu():
    """Afișează meniul interactiv și execută opțiunea aleasă."""
    while True:
        print_banner()
        print(f"{Colors.BOLD}Opțiuni disponibile:{Colors.RESET}")
        print(f"  {Colors.GREEN}{Colors.BOLD}1.{Colors.RESET} {Colors.BOLD}Lansare Completă{Colors.RESET} (Ghid Protocoale + Ghid IRIS + Asistent AI + Panou Admin) {Colors.DIM}[Recomandat]{Colors.RESET}")
        print(f"  {Colors.CYAN}2.{Colors.RESET} Doar Ghidul Protocoalelor & IRIS (MkDocs — Port 8000)")
        print(f"  {Colors.CYAN}3.{Colors.RESET} Panoul de Administrare & Backend AI (Flask — Port 5173)")
        print(f"  {Colors.CYAN}4.{Colors.RESET} Actualizare & Re-generare Indici (Comparison, Sitemap, Forms)")
        print(f"  {Colors.CYAN}5.{Colors.RESET} Rulare Teste Automate (pytest)")
        print(f"  {Colors.CYAN}6.{Colors.RESET} Construire Site Static de Producție (mkdocs build)")
        print(f"  {Colors.DIM}0. Ieșire{Colors.RESET}")
        print()

        try:
            choice = input(f"{Colors.BOLD}Selectați o opțiune [0-6]: {Colors.RESET}").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nLa revedere!")
            break

        if choice == "1":
            run_all(open_browser=True)
            break
        elif choice == "2":
            run_docs(open_browser=True)
            break
        elif choice == "3":
            run_admin(open_browser=True)
            break
        elif choice == "4":
            run_indexes()
            input(f"\n{Colors.DIM}Apăsați Enter pentru a reveni la meniu...{Colors.RESET}")
        elif choice == "5":
            run_tests()
            input(f"\n{Colors.DIM}Apăsați Enter pentru a reveni la meniu...{Colors.RESET}")
        elif choice == "6":
            run_build()
            input(f"\n{Colors.DIM}Apăsați Enter pentru a reveni la meniu...{Colors.RESET}")
        elif choice in ("0", "q", "exit", "quit"):
            print("La revedere!")
            break
        else:
            print(f"{Colors.RED}Opțiune invalidă. Alegeți un număr între 0 și 6.{Colors.RESET}")
            time.sleep(1)


# ---------------------------------------------------------------------------
# Punct de intrare CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Launcher unitar pentru Ghidul Protocoalelor de Radiologie.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--all", "-a", action="store_true", help="Pornește ambele servere (Ghid + Admin)")
    parser.add_argument("--docs", "-d", action="store_true", help="Pornește serverul Ghid Protocoale (port 8000)")
    parser.add_argument("--admin", "-m", action="store_true", help="Pornește Panoul de Administrare (port 5173)")
    parser.add_argument("--index", "-i", action="store_true", help="Re-generează toți indecșii")
    parser.add_argument("--test", "-t", action="store_true", help="Rulează suita de teste (pytest)")
    parser.add_argument("--build", "-b", action="store_true", help="Construiește site-ul static (mkdocs build)")
    parser.add_argument("--no-browser", action="store_true", help="Nu deschide automat browserul")

    args = parser.parse_args()

    # Verifică dependințele
    if not check_dependencies():
        print(f"{Colors.RED}Eroare: dependințele necesare nu sunt disponibile.{Colors.RESET}")
        sys.exit(1)

    open_browser = not args.no_browser

    if args.all:
        run_all(open_browser=open_browser)
    elif args.docs:
        run_docs(open_browser=open_browser)
    elif args.admin:
        run_admin(open_browser=open_browser)
    elif args.index:
        sys.exit(0 if run_indexes() else 1)
    elif args.test:
        sys.exit(run_tests())
    elif args.build:
        sys.exit(run_build())
    else:
        # Fără argumente -> meniu interactiv
        interactive_menu()


if __name__ == "__main__":
    main()
