@echo off
echo Installing Sea - Student Education AI...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org
    pause
    exit /b 1
)

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo ============================================
echo Setup complete!
echo.
echo To start the app, run:
echo   streamlit run app.py
echo.
echo The app will open in your browser at:
echo   http://localhost:8501
echo ============================================
pause
