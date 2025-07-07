@echo off
REM ipip installer for Windows
REM Installs ipip system-wide with proper dependencies

setlocal enabledelayedexpansion

echo.
echo [94m🚀 Installing ipip - Intelligent pip package installer[0m
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [91m[ERROR] Python is not installed or not in PATH.[0m
    echo [93mTip: If you're in a virtual environment, make sure it's activated[0m
    echo [93mOr install Python 3.8+ from https://python.org[0m
    pause
    exit /b 1
)

REM Get Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo [92m[SUCCESS] Python !PYTHON_VERSION! found[0m

REM Check pip
python -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [91m[ERROR] pip is not installed.[0m
    echo [93mPlease install pip first.[0m
    pause
    exit /b 1
)

echo [92m[SUCCESS] pip found[0m

REM Install dependencies
echo [94m[INFO] Installing build dependencies...[0m
python -m pip install --upgrade pip setuptools wheel build

REM Install runtime dependencies
echo [94m[INFO] Installing runtime dependencies...[0m
python -m pip install click>=8.0.0 requests>=2.25.0 rich>=10.0.0 packaging>=21.0

REM Build and install ipip
echo [94m[INFO] Building ipip package...[0m

if exist "pyproject.toml" (
    REM Modern build (build tool already installed above)
    python -m build
    
    REM Find the built wheel
    for /f "delims=" %%i in ('dir /b dist\*.whl 2^>nul') do set WHEEL_FILE=dist\%%i
    
    if "!WHEEL_FILE!"=="" (
        echo [91m[ERROR] Failed to build wheel file[0m
        pause
        exit /b 1
    )
    
    echo [94m[INFO] Installing ipip from wheel: !WHEEL_FILE![0m
    python -m pip install "!WHEEL_FILE!" --force-reinstall
    
) else if exist "setup.py" (
    REM Legacy build
    echo [94m[INFO] Installing ipip from setup.py...[0m
    python -m pip install . --force-reinstall
) else (
    echo [91m[ERROR] No pyproject.toml or setup.py found.[0m
    echo [93mAre you in the ipip directory?[0m
    pause
    exit /b 1
)

REM Verify installation
echo [94m[INFO] Verifying installation...[0m
ipip --help >nul 2>&1
if %errorlevel% neq 0 (
    echo [91m[ERROR] Installation failed. ipip command not found.[0m
    echo [93m[INFO] Try adding Python Scripts to your PATH[0m
    pause
    exit /b 1
)

echo [92m[SUCCESS] ipip successfully installed![0m
echo.
echo [94m[INFO] Testing basic functionality...[0m
ipip --help >nul
echo [92m[SUCCESS] ipip is working correctly![0m
echo.
echo [92m🎉 Installation complete![0m
echo.
echo [94m[INFO] Running first-time setup...[0m
python -c "from ipip.ollama_installer import OllamaInstaller; OllamaInstaller(verbose=True).interactive_setup()"

echo.
echo [94m[INFO] Try these commands:[0m
echo   ipip blender --dry-run
echo   ipip "computer vision" --dry-run
echo   ipip --verbose "build a chatbot" --dry-run
echo   ipip "move test files to tests folder" --dry-run

echo.
echo Press any key to exit...
pause >nul