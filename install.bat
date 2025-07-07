@echo off
REM ipip installer for Windows
REM Installs ipip system-wide with proper dependencies

setlocal enabledelayedexpansion

echo.
echo [94m🚀 Installing ipip - Intelligent pip package installer[0m
echo.

REM Find Python executable
set PYTHON_CMD=""
set PYTHON_VERSION=""

REM Try different Python commands in order of preference
echo [94m[INFO] Looking for Python installation...[0m

REM Try py launcher first (recommended for Windows)
py --version >nul 2>&1
if %errorlevel% equ 0 (
    set PYTHON_CMD=py
    for /f "tokens=2" %%i in ('py --version 2^>^&1') do set PYTHON_VERSION=%%i
    goto :python_found
)

REM Try python3
python3 --version >nul 2>&1
if %errorlevel% equ 0 (
    set PYTHON_CMD=python3
    for /f "tokens=2" %%i in ('python3 --version 2^>^&1') do set PYTHON_VERSION=%%i
    goto :python_found
)

REM Try python (but check it's not the Microsoft Store stub)
python --version >nul 2>&1
if %errorlevel% equ 0 (
    REM Check if it's the real Python or Microsoft Store stub
    python -c "import sys; print('real')" >nul 2>&1
    if %errorlevel% equ 0 (
        set PYTHON_CMD=python
        for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
        goto :python_found
    )
)

REM No Python found
echo [91m[ERROR] Python is not installed or not accessible.[0m
echo [93m[HELP] Please install Python 3.8+ from https://python.org[0m
echo [93m[HELP] Make sure to check "Add Python to PATH" during installation[0m
echo [93m[HELP] Or if you have Python installed, try running as administrator[0m
echo.
echo [94m[INFO] You can also try using the Python Launcher:[0m
echo [94m  py --version[0m
echo.
pause
exit /b 1

:python_found
echo [92m[SUCCESS] Python !PYTHON_VERSION! found using !PYTHON_CMD![0m

REM Check Python version is 3.8+
for /f "tokens=1,2 delims=." %%a in ("!PYTHON_VERSION!") do (
    set MAJOR=%%a
    set MINOR=%%b
)

if !MAJOR! LSS 3 (
    echo [91m[ERROR] Python 3.8+ is required. Found: !PYTHON_VERSION![0m
    pause
    exit /b 1
)

if !MAJOR! EQU 3 if !MINOR! LSS 8 (
    echo [91m[ERROR] Python 3.8+ is required. Found: !PYTHON_VERSION![0m
    pause
    exit /b 1
)

REM Check pip
!PYTHON_CMD! -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [91m[ERROR] pip is not installed.[0m
    echo [93mPlease install pip first.[0m
    pause
    exit /b 1
)

echo [92m[SUCCESS] pip found[0m

REM Install dependencies
echo [94m[INFO] Installing build dependencies...[0m
!PYTHON_CMD! -m pip install --upgrade pip setuptools wheel build

REM Install runtime dependencies
echo [94m[INFO] Installing runtime dependencies...[0m
!PYTHON_CMD! -m pip install click>=8.0.0 requests>=2.25.0 rich>=10.0.0 packaging>=21.0

REM Clean previous builds
echo [94m[INFO] Cleaning previous builds...[0m
if exist "dist" rmdir /s /q "dist" >nul 2>&1
if exist "build" rmdir /s /q "build" >nul 2>&1
if exist "ipip.egg-info" rmdir /s /q "ipip.egg-info" >nul 2>&1

REM Build and install ipip
echo [94m[INFO] Building ipip package...[0m

if exist "pyproject.toml" (
    REM Modern build using build module directly (skip custom build.py)
    echo [94m[INFO] Building wheel with python -m build...[0m
    !PYTHON_CMD! -m build --wheel --outdir dist
    
    REM Find the built wheel
    for /f "delims=" %%i in ('dir /b dist\*.whl 2^>nul') do set WHEEL_FILE=dist\%%i
    
    if "!WHEEL_FILE!"=="" (
        echo [91m[ERROR] Failed to build wheel file[0m
        echo [93m[INFO] Trying direct installation instead...[0m
        !PYTHON_CMD! -m pip install . --force-reinstall
        goto :verify_installation
    )
    
    echo [94m[INFO] Installing ipip from wheel: !WHEEL_FILE![0m
    !PYTHON_CMD! -m pip install "!WHEEL_FILE!" --force-reinstall
    
) else if exist "setup.py" (
    REM Legacy build
    echo [94m[INFO] Installing ipip from setup.py...[0m
    !PYTHON_CMD! -m pip install . --force-reinstall
) else (
    echo [91m[ERROR] No pyproject.toml or setup.py found.[0m
    echo [93mAre you in the ipip directory?[0m
    pause
    exit /b 1
)

:verify_installation
REM Verify installation
echo [94m[INFO] Verifying installation...[0m
ipip --help >nul 2>&1
if %errorlevel% neq 0 (
    echo [91m[ERROR] Installation failed. ipip command not found.[0m
    echo [93m[INFO] Try adding Python Scripts to your PATH[0m
    echo [93m[INFO] Or use: !PYTHON_CMD! -m ipip --help[0m
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
!PYTHON_CMD! -c "from ipip.ollama_installer import OllamaInstaller; OllamaInstaller(verbose=True).interactive_setup()"

echo.
echo [94m[INFO] Try these commands:[0m
echo   ipip blender --dry-run
echo   ipip "computer vision" --dry-run
echo   ipip --verbose "build a chatbot" --dry-run
echo   ipip "move test files to tests folder" --dry-run

echo.
echo Press any key to exit...
pause >nul