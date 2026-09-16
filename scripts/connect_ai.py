"""Interactive login helper, opened explicitly by the editor's Connect button."""
import os
import subprocess
import sys
import tempfile
from cli_ai import cli_command, oauth_environment, gemini_settings, resolve_gemini_cli


def main():
    provider = sys.argv[1] if len(sys.argv) == 2 else ''
    if provider not in ('gemini_oauth', 'codex_oauth'):
        raise SystemExit('Furnizor invalid.')
    name = 'codex' if provider == 'codex_oauth' else resolve_gemini_cli()
    print('Conectare cont AI pentru editorul de radiologie. Finalizati autentificarea in browser.')
    env = oauth_environment()
    with tempfile.TemporaryDirectory(prefix='radiology-login-') as directory:
        command = cli_command(name)
        if name == 'codex':
            command += ['login']
        elif name == 'agy':
            print('Antigravity CLI (agy) este gata de utilizare. Dacă este necesară re-autentificarea, urmați instrucțiunile din terminal. Ieșiți cu /quit sau Ctrl+C.')
        else:
            env['GEMINI_CLI_SYSTEM_SETTINGS_PATH'] = str(gemini_settings(directory, False))
            command += ['--extensions', 'none']
            print('Alegeti Sign in with Google. Dupa conectare, inchideti Gemini cu /quit.')
        subprocess.call(command, env=env, cwd=directory)
    input('Reveniti in editor si apasati Verifica conexiunea. Enter pentru inchidere...')


if __name__ == '__main__':
    main()
