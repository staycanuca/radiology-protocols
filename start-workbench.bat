@echo off
cd /d "%~dp0"
python -m protocol_workbench.app %*
pause
