# ipip Quick Start Guide

## Option 1: Quick Test (Core Functionality Only)

Test ipip's core logic without installing dependencies:

```bash
# Windows
cd C:\Users\AGIA\OneDrive\Documents\ipip
python minimal_test.py

# Linux/Mac  
cd /path/to/ipip
python3 minimal_test.py
```

This tests the package resolution logic without requiring external dependencies.

## Option 2: Full Installation and Testing

### Step 1: Install Dependencies

```bash
# Automated dependency installation
python install_deps.py

# Or manual installation:
pip install click requests rich packaging

# For building:
pip install build twine wheel
```

### Step 2: Test Full Functionality

```bash
# Windows
python -m ipip.cli --help
python -m ipip.cli blender --dry-run
python -m ipip.cli "vision recognition" --dry-run

# Linux/Mac
python3 -m ipip.cli --help  
python3 -m ipip.cli blender --dry-run
python3 -m ipip.cli "vision recognition" --dry-run
```

### Step 3: Install ipip Package

```bash
# Virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -e .

# Test installed version
ipip --help
ipip blender --dry-run
```

## Option 3: Build for PyPI

```bash
# Automated build
python build.py

# Or manual build:
python -m build
python -m twine check dist/*
```

## Expected Outputs

### Core Resolution Test:
```
ipip blender --dry-run
# Expected: Would install bpy

ipip pil --dry-run  
# Expected: Would install pillow

ipip opencv --dry-run
# Expected: Would install opencv-python
```

### Package Discovery:
```
ipip "vision recognition" --dry-run
# Expected: Would install opencv-python, pillow, scikit-image

ipip "machine learning" --dry-run
# Expected: Would install scikit-learn, pandas, numpy
```

### Requirements Generation:
```
echo "import requests, pandas" > test.py
ipip "create requirements"
# Expected: Creates requirements.txt with project dependencies
```

## Troubleshooting

### "No module named 'click'"
```bash
pip install click requests rich packaging
```

### "Command not found: python"
Try `python3` instead of `python`, or vice versa.

### "Permission denied" (Windows)
Run Command Prompt as Administrator or use virtual environment.

### CLI not working after installation
Make sure you're in the right virtual environment:
```bash
which ipip        # Linux/Mac
where ipip        # Windows
```

## Ready to Use!

Once dependencies are installed, your ipip package provides:

✅ **Smart package resolution**: `ipip blender` → `bpy`  
✅ **Natural language commands**: `ipip create requirements`  
✅ **Package discovery**: `ipip vision recognition`  
✅ **Dry-run mode**: `--dry-run` to see what would be installed  
✅ **Verbose output**: `--verbose` for detailed information  

Your intelligent pip installer is ready! 🚀