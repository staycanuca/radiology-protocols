@echo off
chcp 65001 >nul
cd /d "%~dp0"
python run.py %*
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo A aparut o eroare la executia aplicatiei.
    pause
)
