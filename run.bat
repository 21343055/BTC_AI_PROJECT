@echo off
REM Run main.py using the project's virtual environment
cd /d "%~dp0"
".\.venv\Scripts\python.exe" main.py
pause
