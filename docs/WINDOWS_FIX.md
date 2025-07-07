# Windows Unicode Error Fix

## 🐛 **Error Encountered**

```
UnicodeDecodeError: 'charmap' codec can't decode byte 0x8d in position 426: character maps to <undefined>
```

## ✅ **Problem Fixed**

The issue was that `setup.py` was trying to read `README.md` without specifying UTF-8 encoding, causing Windows (which uses cp1252 by default) to fail on Unicode characters.

## 🛠️ **Fix Applied**

**Old code:**
```python
long_description=open("README.md").read(),
```

**New code:**
```python
def read_readme():
    try:
        with open("README.md", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Intelligent pip package installer using AI to resolve package names"

long_description=read_readme(),
```

## 🚀 **Now Try Building Again**

**Option 1: Quick test**
```cmd
python setup.py --version
```

**Option 2: Build wheel**
```cmd
python -m pip wheel . --no-deps --wheel-dir dist
```

**Option 3: Use Windows build script**
```cmd
python windows_build.py
```

## 💡 **Additional Windows Tips**

If you still get encoding errors:

1. **Set UTF-8 environment variable:**
   ```cmd
   set PYTHONUTF8=1
   python -m pip wheel . --no-deps --wheel-dir dist
   ```

2. **Use PowerShell instead of Command Prompt:**
   ```powershell
   $env:PYTHONUTF8="1"
   python -m pip wheel . --no-deps --wheel-dir dist
   ```

3. **Virtual environment (recommended):**
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   pip install build wheel
   python -m pip wheel . --no-deps --wheel-dir dist
   ```

## ⏱️ **Expected Build Time**

- **Setup test:** ~2 seconds
- **Wheel build:** ~60-90 seconds (first time)
- **Subsequent builds:** ~30 seconds

## 🎯 **Success Indicators**

**Build successful when you see:**
```
Successfully built ipip
Created wheel for ipip: filename=ipip-0.1.0-py3-none-any.whl
```

**Verify result:**
```cmd
dir dist\
# Should show: ipip-0.1.0-py3-none-any.whl
```

The Unicode encoding fix should resolve the Windows build issue! 🎉