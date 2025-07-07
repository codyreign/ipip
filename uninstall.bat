@echo off
REM ipip uninstaller for Windows

echo.
echo [94m🗑️  Uninstalling ipip...[0m
echo.

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [91m[ERROR] Python not found in PATH[0m
    pause
    exit /b 1
)

REM Check if ipip is installed
ipip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [93m[WARNING] ipip is not installed or not in PATH[0m
) else (
    echo [94m[INFO] Found ipip installation[0m
)

REM Uninstall using pip
echo [94m[INFO] Removing ipip package...[0m
python -m pip uninstall ipip -y

REM Verify uninstallation
ipip --version >nul 2>&1
if %errorlevel% equ 0 (
    echo [93m[WARNING] ipip command still found in PATH[0m
    echo [94m[INFO] You may need to restart your terminal[0m
) else (
    echo [92m[SUCCESS] ipip successfully uninstalled![0m
)

echo.
echo [92m✅ Uninstallation complete![0m
echo.
echo [94m[INFO] Thank you for using ipip! 👋[0m
echo.
pause