# 🚀 ipip Installation Guide

This guide provides multiple ways to install ipip system-wide from the repository.

## 📥 Method 1: One-Line Install (Recommended)

### Windows
```cmd
curl -o install.bat https://raw.githubusercontent.com/yourusername/ipip/main/install.bat && install.bat
```

### Unix/Linux/macOS  
```bash
curl -sSL https://raw.githubusercontent.com/yourusername/ipip/main/install.sh | bash
```

## 📦 Method 2: Clone and Install

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/ipip.git
cd ipip
```

### Step 2: Run Installer

**Windows:**
```cmd
install.bat
```

**Unix/Linux/macOS:**
```bash
chmod +x install.sh
./install.sh
```

## 🔧 Method 3: Using Make

```bash
git clone https://github.com/yourusername/ipip.git
cd ipip
make install
```

## 🐍 Method 4: Direct pip Install

**From GitHub:**
```bash
pip install git+https://github.com/yourusername/ipip.git
```

**Local Development:**
```bash
git clone https://github.com/yourusername/ipip.git
cd ipip
pip install .
```

## ✅ Verify Installation

After installation, test ipip:

```bash
# Check installation
ipip --help

# Test basic functionality
ipip blender --dry-run

# Test AI features (if Ollama installed)
ipip --verbose "build a chatbot" --dry-run
```

## 🤖 AI Features Setup (Optional)

For AI-powered package resolution:

1. **Install Ollama:** https://ollama.ai/
2. **Install a text model:**
   ```bash
   ollama pull llama3.2
   ```
3. **Test AI features:**
   ```bash
   ipip --verbose "sentiment analysis" --dry-run
   ```

## 🗑️ Uninstallation

### Using Uninstaller Scripts
```bash
# Unix/Linux/macOS
./uninstall.sh

# Windows
uninstall.bat
```

### Using Make
```bash
make uninstall
```

### Using pip
```bash
pip uninstall ipip
```

## 🔧 Development Installation

For contributing to ipip:

```bash
git clone https://github.com/yourusername/ipip.git
cd ipip
make install-dev
```

This installs ipip in editable mode, so changes to source code take effect immediately.

## 🚨 Troubleshooting

### Python Not Found
- Install Python 3.8+ from https://python.org
- Ensure Python is in your PATH

### Permission Errors
```bash
# Install to user directory instead
pip install --user git+https://github.com/yourusername/ipip.git
```

### Ollama Not Detected
- Install Ollama from https://ollama.ai/
- Ensure `ollama` command is in PATH
- Install a text model: `ollama pull llama3.2`

### ipip Command Not Found
- Check if `~/.local/bin` is in PATH (Unix)
- Check if Python Scripts directory is in PATH (Windows)
- Restart terminal after installation

## 🎯 Quick Start After Installation

```bash
# Install packages intelligently
ipip blender              # → bpy
ipip opencv              # → opencv-python  
ipip "computer vision"   # → multiple CV packages

# Use AI features
ipip "build a chatbot"   # → AI suggests relevant packages

# Generate requirements
ipip create requirements # → scans project, creates requirements.txt
```

## 📊 Installation Methods Comparison

| Method | Pros | Cons | Best For |
|--------|------|------|----------|
| One-line install | Fastest, automatic | Requires internet | Most users |
| Clone + installer | Full control, offline | Manual steps | Power users |
| Make install | Clean, standard | Requires make | Developers |
| pip install | Simple, familiar | No extras | Basic installs |

Choose the method that best fits your needs! 🚀