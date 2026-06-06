# Run main.py using the project's virtual environment
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir
& ".\.venv\Scripts\python.exe" main.py
