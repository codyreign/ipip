# 🔧 Windows Installation Troubleshooting

Common issues and solutions for installing ipip on Windows.

## 🚫 "Python was not found; run without arguments to install from the Microsoft Store"

### Problem
Windows 10/11 has app execution aliases that redirect `python` to the Microsoft Store instead of your actual Python installation.

### Solutions

#### Solution 1: Use the Fixed Installer (Recommended)
```cmd
# Use the improved installer that handles this automatically
install_windows_fixed.bat
```

#### Solution 2: Disable App Execution Aliases
1. Press `Win + I` to open Settings
2. Go to `Apps` → `Advanced app settings` → `App execution aliases`
3. Turn OFF the toggles for:
   - `App Installer python.exe`
   - `App Installer python3.exe`

#### Solution 3: Use Python Launcher
```cmd
# Check if py launcher works
py --version

# If it works, use:
py -m pip install ipip
```

#### Solution 4: Use Full Path to Python
```cmd
# Find your Python installation
where python

# Use full path (example):
C:\Python39\python.exe -m pip install ipip
```

## 🚫 "pip is not installed"

### Problem
Python is found but pip is missing.

### Solutions

#### Solution 1: Reinstall Python with pip
1. Go to https://python.org/downloads/
2. Download latest Python 3.8+
3. **Check "Add Python to PATH"**
4. **Check "pip"** in optional features
5. Install

#### Solution 2: Install pip manually
```cmd
# Download get-pip.py
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

# Install pip
python get-pip.py
```

## 🚫 "ipip command not found" after installation

### Problem
ipip installed but command not available in PATH.

### Solutions

#### Solution 1: Add Python Scripts to PATH
1. Find your Python Scripts directory:
   ```cmd
   python -c "import sys; print(sys.prefix + '\\Scripts')"
   ```
2. Add that path to your PATH environment variable
3. Restart Command Prompt

#### Solution 2: Use module syntax
```cmd
# Instead of: ipip --help
# Use:
python -m ipip --help
```

#### Solution 3: Create batch file (Quick fix)
```cmd
# Create ipip.bat in a directory that's in PATH
echo @python -m ipip %* > C:\Windows\ipip.bat
```

## 🚫 "Access denied" or permission errors

### Problem
Installation fails due to permissions.

### Solutions

#### Solution 1: Run as Administrator
1. Right-click Command Prompt
2. Select "Run as administrator"
3. Run installer again

#### Solution 2: User installation
```cmd
# Install just for current user
python -m pip install ipip --user
```

#### Solution 3: Virtual environment
```cmd
# Create virtual environment
python -m venv ipip_env

# Activate it
ipip_env\Scripts\activate

# Install ipip
pip install ipip
```

## 🚫 Build fails with "Failed to build wheel"

### Problem
Package build process fails.

### Solutions

#### Solution 1: Use direct installation
```cmd
# Skip wheel building
python -m pip install . --no-build-isolation
```

#### Solution 2: Install build tools
```cmd
# Install Microsoft C++ Build Tools
# Download from: https://visualstudio.microsoft.com/visual-cpp-build-tools/

# Or install via chocolatey:
choco install visualstudio2019buildtools
```

#### Solution 3: Use pre-built package (once published)
```cmd
# Install from PyPI instead
pip install ipip
```

## 🚫 Ollama setup fails

### Problem
AI model installation fails.

### Solutions

#### Solution 1: Manual Ollama installation
```cmd
# Download Ollama for Windows
# From: https://ollama.ai/download

# Install a model
ollama pull llama3.2
```

#### Solution 2: Skip Ollama for now
```cmd
# Install ipip without AI features
pip install ipip

# Configure to use remote AI later
ipip --setup
```

#### Solution 3: Use different model
```cmd
# Try smaller model
ollama pull llama3.2:1b

# Or larger model if you have resources
ollama pull llama3.2:8b
```

## 🚫 Unicode/encoding errors

### Problem
Installation fails with encoding errors.

### Solutions

#### Solution 1: Set encoding
```cmd
# Set UTF-8 encoding
set PYTHONIOENCODING=utf-8

# Run installer
install.bat
```

#### Solution 2: Use English locale
```cmd
# Set English locale temporarily
set LANG=en_US.UTF-8

# Run installer
install.bat
```

## 🔍 Diagnostic Commands

Use these to troubleshoot:

```cmd
# Check Python
python --version
py --version
python3 --version

# Check pip
python -m pip --version
py -m pip --version

# Check PATH
echo %PATH%

# Check Python location
where python
where py

# Check installed packages
pip list | findstr ipip

# Test ipip
python -c "import ipip; print('ipip found')"
```

## 📞 Getting Help

If none of these solutions work:

1. **Check GitHub Issues**: https://github.com/codyreign/ipip/issues
2. **Create New Issue** with:
   - Windows version (`winver`)
   - Python version (`python --version`)
   - Error message (full text)
   - Command you ran

3. **Discord/Community**: Ask in Python Discord or Stack Overflow with tags `python-packaging` and `windows`

## 🎯 Quick Fix Summary

**Most Common Solution:**
```cmd
# Try the py launcher
py -m pip install ipip

# Then run
py -m ipip --help
```

**If that doesn't work:**
1. Use `install_windows_fixed.bat`
2. Disable Microsoft Store Python aliases
3. Reinstall Python with "Add to PATH" checked

---

**💡 Tip**: The `py` launcher is usually the most reliable way to run Python on Windows!