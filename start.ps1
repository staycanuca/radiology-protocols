# start.ps1 — Launcher PowerShell pentru Ghidul Protocoalelor de Radiologie
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Set-Location $PSScriptRoot
python run.py $args
