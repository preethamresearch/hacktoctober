# NeuroGrid ScriptSense - Run Script
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "NeuroGrid ScriptSense" -ForegroundColor Cyan
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Checking Python installation..." -ForegroundColor Yellow
python --version
Write-Host ""
Write-Host "Starting Streamlit application..." -ForegroundColor Green
Write-Host ""
Write-Host "The app will open in your default browser." -ForegroundColor Green
Write-Host "Press Ctrl+C to stop the server." -ForegroundColor Yellow
Write-Host ""
streamlit run main.py
