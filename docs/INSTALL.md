# Installation and Testing Guide for ipip

## Quick Start

### Option 1: Using pipx (Recommended)
```bash
# Install pipx if you don't have it
sudo apt install pipx  # or: pip install --user pipx

# Install ipip from local directory
pipx install .

# Test it
ipip --help
ipip blender --dry-run
```

### Option 2: Using Virtual Environment
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install ipip in development mode
pip install -e .

# Test it
ipip --help
ipip blender --dry-run
```

### Option 3: Direct Python Execution (No Installation)
```bash
# Run directly from source
python3 -m ipip.cli --help
python3 -m ipip.cli blender --dry-run
python3 -m ipip.cli vision recognition
```

## Testing the Features

### 1. Test Package Resolution
```bash
# Test common package mappings
ipip blender --dry-run          # Should resolve to 'bpy'
ipip pil --dry-run              # Should resolve to 'pillow'
ipip opencv --dry-run           # Should resolve to 'opencv-python'
ipip sklearn --dry-run          # Should resolve to 'scikit-learn'
```

### 2. Test Package Discovery
```bash
# Test package search
ipip vision recognition         # Shows computer vision packages
ipip machine learning          # Shows ML libraries
ipip web scraping              # Shows web scraping tools
ipip database tools            # Shows database packages
```

### 3. Test Requirements Generation
```bash
# Create a test Python project
mkdir test_project
cd test_project
echo "import requests, pandas, numpy" > main.py
echo "from PIL import Image" >> main.py

# Generate requirements
ipip create requirements
cat requirements.txt
```

### 4. Test Verbose Mode
```bash
# See detailed output
ipip --verbose blender --dry-run
ipip --verbose vision recognition
```

### 5. Test Different Models
```bash
# Test with local model (default)
ipip --model local blender --dry-run

# Test with other models (will fallback to heuristics)
ipip --model openai blender --dry-run
```

## Running Tests

### Install Development Dependencies
```bash
# In virtual environment
pip install -e ".[dev]"

# Or install test dependencies manually
pip install pytest pytest-cov
```

### Run Test Suite
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=ipip

# Run specific test file
pytest tests/test_llm_resolver.py

# Run with verbose output
pytest -v
```

### Test Individual Components
```bash
# Test LLM resolver
python3 -c "
from ipip.llm_resolver import LLMResolver
resolver = LLMResolver(verbose=True)
print('Testing blender:', resolver.resolve_packages('blender'))
print('Testing vision:', resolver.resolve_packages('vision recognition'))
"

# Test package installer (dry run)
python3 -c "
from ipip.package_installer import PackageInstaller
installer = PackageInstaller(dry_run=True, verbose=True)
installer.install_packages(['requests', 'pandas'])
"
```

## Setting Up Ollama (Optional)

For the best LLM experience, install Ollama:

```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Pull a model
ollama pull llama3.2

# Test with ipip
ipip --verbose blender --dry-run
```

## Real Installation Examples

Once you're confident it works:

```bash
# Install actual packages
ipip blender              # Installs bpy
ipip opencv               # Installs opencv-python
ipip "web api framework"  # Shows FastAPI, Flask, etc.
```

## Configuration

Create config file:
```bash
mkdir -p ~/.config/ipip
cat > ~/.config/ipip/config.json << 'EOF'
{
  "llm": {
    "model": "local",
    "timeout": 30
  },
  "verbose": false,
  "dry_run_default": false,
  "package_search_limit": 10
}
EOF
```

## Troubleshooting

### Common Issues

1. **"externally-managed-environment" error**
   - Use pipx or virtual environment
   - Don't use system pip directly

2. **"command not found: ipip"**
   - Make sure you're in the right virtual environment
   - Or use `python3 -m ipip.cli` instead

3. **LLM not working**
   - Check if Ollama is installed: `ollama --version`
   - ipip will fallback to heuristics automatically

4. **Import errors**
   - Make sure all dependencies are installed: `pip install -e .`
   - Check Python path: `python3 -c "import ipip; print(ipip.__file__)"`

### Debug Mode
```bash
# Run with maximum verbosity
ipip --verbose blender --dry-run

# Check configuration
python3 -c "
from ipip.config import ConfigManager
ConfigManager().show_config()
"
```