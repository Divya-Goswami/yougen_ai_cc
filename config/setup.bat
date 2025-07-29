@echo off
REM YouGen AI YouTube Content Generator - Windows Setup Script
REM For Envato Buyers - One-Click Installation

echo.
echo 🎬 YouGen AI YouTube Content Generator
echo ==========================================
echo 🚀 Automated Setup for Windows Users
echo.

setlocal enabledelayedexpansion

REM Check if Python is installed
echo [INFO] Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python not found. Please install Python 3.8+ from https://python.org
    echo [INFO] After installing Python, run this script again.
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo [SUCCESS] Python %PYTHON_VERSION% found

REM Check Python version
for /f "tokens=2 delims=." %%i in ("%PYTHON_VERSION%") do set PYTHON_MAJOR=%%i
for /f "tokens=3 delims=." %%i in ("%PYTHON_VERSION%") do set PYTHON_MINOR=%%i

if %PYTHON_MAJOR% LSS 3 (
    echo [ERROR] Python 3.8+ required. Current version: %PYTHON_VERSION%
    pause
    exit /b 1
)

if %PYTHON_MAJOR% EQU 3 (
    if %PYTHON_MINOR% LSS 8 (
        echo [ERROR] Python 3.8+ required. Current version: %PYTHON_VERSION%
        pause
        exit /b 1
    )
)

REM Create virtual environment
echo [INFO] Creating Python virtual environment...
if exist venv (
    echo [WARNING] Virtual environment already exists. Removing old one...
    rmdir /s /q venv
)

python -m venv venv
if %errorlevel% neq 0 (
    echo [ERROR] Failed to create virtual environment
    pause
    exit /b 1
)
echo [SUCCESS] Virtual environment created

REM Activate virtual environment
echo [INFO] Activating virtual environment...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo [ERROR] Failed to activate virtual environment
    pause
    exit /b 1
)
echo [SUCCESS] Virtual environment activated

REM Upgrade pip
echo [INFO] Upgrading pip...
python -m pip install --upgrade pip
echo [SUCCESS] Pip upgraded

REM Install Python dependencies
echo [INFO] Installing Python dependencies...
if exist requirements.txt (
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo [ERROR] Failed to install dependencies
        pause
        exit /b 1
    )
    echo [SUCCESS] Python dependencies installed
) else (
    echo [ERROR] requirements.txt not found
    pause
    exit /b 1
)

REM Check if Ollama is installed
echo [INFO] Checking Ollama installation...
ollama --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [INFO] Ollama not found. Please download and install from https://ollama.ai/download
    echo [INFO] After installing Ollama, run this script again.
    pause
    exit /b 1
)
echo [SUCCESS] Ollama found

REM Start Ollama service
echo [INFO] Starting Ollama service...
start /B ollama serve
timeout /t 5 /nobreak >nul
echo [SUCCESS] Ollama service started

REM Download AI model
echo [INFO] Downloading AI model (this may take a few minutes)...
ollama pull gemma:2b
if %errorlevel% neq 0 (
    echo [ERROR] Failed to download AI model
    pause
    exit /b 1
)
echo [SUCCESS] AI model downloaded

REM Create .env file
echo [INFO] Creating configuration file...
if not exist .env (
    python -c "import secrets; print('SECRET_KEY=' + secrets.token_hex(32))" > .env
    echo FLASK_DEBUG=True >> .env
    echo PORT=5000 >> .env
    echo [SUCCESS] Configuration file created
) else (
    echo [SUCCESS] Configuration file already exists
)

REM Create start script
echo [INFO] Creating start script...
(
echo @echo off
echo echo 🎬 Starting YouGen AI YouTube Content Generator...
echo echo.
echo call venv\Scripts\activate.bat
echo python app.py
echo pause
) > start.bat
echo [SUCCESS] Start script created

REM Create stop script
echo [INFO] Creating stop script...
(
echo @echo off
echo echo 🛑 Stopping YouGen AI YouTube Content Generator...
echo taskkill /f /im python.exe 2^>nul
echo taskkill /f /im ollama.exe 2^>nul
echo echo ✅ Application stopped
echo pause
) > stop.bat
echo [SUCCESS] Stop script created

REM Final success message
echo.
echo 🎉 SETUP COMPLETE!
echo ==================
echo.
echo ✅ Your AI YouTube Content Generator is ready to use!
echo.
echo 🚀 To start the application:
echo    start.bat
echo.
echo 🌐 Open your browser and go to:
echo    http://localhost:5000
echo.
echo 🛑 To stop the application:
echo    stop.bat
echo.
echo 📚 For detailed instructions, see:
echo    - INSTALLATION.md (Quick guide^)
echo    - README.md (Complete documentation^)
echo.
echo 🎬 Start creating viral YouTube content now!
echo.
echo Need help? Contact: support@YouGen.com
echo.

REM Optional: Start the application
set /p START_NOW="Would you like to start the application now? (y/n): "
if /i "%START_NOW%"=="y" (
    echo 🚀 Starting application...
    call start.bat
)

pause 