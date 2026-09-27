@echo off
title Deploy Cloudflare Pages - protocoale
cd /d "%~dp0"
python deploy_cloudflare.py %*
pause
