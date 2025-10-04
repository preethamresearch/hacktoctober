@echo off
echo ===============================================
echo NeuroGrid ScriptSense
echo ===============================================
echo.
echo Checking Python installation...
python --version
echo.
echo Starting Streamlit application...
echo.
echo The app will open in your default browser.
echo Press Ctrl+C to stop the server.
echo.
streamlit run main.py
