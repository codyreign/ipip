# Windows Installation Guide for ipip

## Quick Test (No Installation)

Open Command Prompt or PowerShell in the ipip directory:

```cmd
cd C:\Users\AGIA\OneDrive\Documents\ipip

# Run basic tests
python test_basic.py

# Test the CLI directly
python -m ipip.cli --help
python -m ipip.cli blender --dry-run
python -m ipip.cli "vision recognition" --dry-run
```

## Option 1: Virtual Environment (Recommended)

```cmd
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate

# Install ipip in development mode
pip install -e .

# Test it
ipip --help
ipip blender --dry-run
ipip "machine learning" --dry-run
```

## Option 2: Using pipx

```cmd
# Install pipx first
pip install --user pipx

# Add pipx to PATH (one time setup)
python -m pipx ensurepath

# Install ipip
pipx install .

# Test it
ipip --help
ipip opencv --dry-run
```

## Option 3: Direct Installation (Not Recommended)

```cmd
# If you really want to install globally
pip install -e .

# Test it
ipip --help
```

## Building for PyPI

```cmd
# Run the build script
python build.py

# Or manually:
pip install build twine wheel
python -m build
python -m twine check dist/*
```

## Testing Examples

```cmd
# Test package resolution
ipip blender --dry-run              # Should show: bpy
ipip pil --dry-run                  # Should show: pillow
ipip opencv --dry-run               # Should show: opencv-python

# Test package discovery
ipip "search computer vision"       # Shows vision packages
ipip "machine learning tools"       # Shows ML packages

# Test requirements generation
echo import requests, pandas > test.py
ipip "create requirements"
type requirements.txt
```

## Common Windows Issues

### 1. Python not found
Make sure Python is in your PATH:
```cmd
python --version
```
If not found, reinstall Python with "Add to PATH" checked.

### 2. pip not found
```cmd
python -m pip --version
```

### 3. Virtual environment activation issues
Use full path:
```cmd
C:\path\to\your\project\venv\Scripts\activate
```

### 4. Permission errors
Run Command Prompt as Administrator, or use `--user` flag:
```cmd
pip install --user -e .
```

### 5. Unicode errors in output
The CLI should work fine now, but if you see encoding issues:
```cmd
chcp 65001  # Enable UTF-8 in Command Prompt
```

## Configuration

Create config directory:
```cmd
mkdir %APPDATA%\ipip
echo { > %APPDATA%\ipip\config.json
echo   "llm": { >> %APPDATA%\ipip\config.json
echo     "model": "local" >> %APPDATA%\ipip\config.json
echo   } >> %APPDATA%\ipip\config.json
echo } >> %APPDATA%\ipip\config.json
```

## Real Usage Examples

Once installed:

```cmd
# Install packages intelligently
ipip blender              # Installs bpy
ipip image processing     # Shows pillow, opencv-python, etc.
ipip web framework        # Shows flask, django, fastapi

# Generate requirements for your project
cd your_python_project
ipip create requirements
```

Your ipip package is now ready to use on Windows! 🚀