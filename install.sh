#!/bin/bash
# ipip installer for Unix/Linux/macOS
# Installs ipip system-wide with proper dependencies

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Print colored output
print_info() { echo -e "${BLUE}[INFO]${NC} $1"; }
print_success() { echo -e "${GREEN}[SUCCESS]${NC} $1"; }
print_warning() { echo -e "${YELLOW}[WARNING]${NC} $1"; }
print_error() { echo -e "${RED}[ERROR]${NC} $1"; }

# Check if running as root (not recommended)
if [[ $EUID -eq 0 ]]; then
   print_warning "Running as root. Consider using --user flag for pip install."
fi

print_info "🚀 Installing ipip - Intelligent pip package installer"
echo

# Check Python version
print_info "Checking Python installation..."
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    print_error "Python is not installed. Please install Python 3.8+ first."
    exit 1
fi

# Determine Python command
PYTHON_CMD="python3"
if ! command -v python3 &> /dev/null; then
    PYTHON_CMD="python"
fi

# Check Python version
PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | grep -oE '[0-9]+\.[0-9]+')
PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

if [[ $PYTHON_MAJOR -lt 3 ]] || [[ $PYTHON_MAJOR -eq 3 && $PYTHON_MINOR -lt 8 ]]; then
    print_error "Python 3.8+ is required. Found: $($PYTHON_CMD --version)"
    exit 1
fi

print_success "Python $($PYTHON_CMD --version | grep -oE '[0-9]+\.[0-9]+\.[0-9]+') found"

# Check pip
print_info "Checking pip installation..."
if ! $PYTHON_CMD -m pip --version &> /dev/null; then
    print_error "pip is not installed. Please install pip first."
    exit 1
fi

print_success "pip found"

# Install dependencies first
print_info "Installing build dependencies..."
$PYTHON_CMD -m pip install --upgrade pip setuptools wheel build

print_info "Installing runtime dependencies..."
$PYTHON_CMD -m pip install 'click>=8.0.0' 'requests>=2.25.0' 'rich>=10.0.0' 'packaging>=21.0'

# Build and install ipip
print_info "Building ipip package..."
if [[ -f "pyproject.toml" ]]; then
    # Modern build (build tool already installed above)
    $PYTHON_CMD -m build
    
    # Find the built wheel
    WHEEL_FILE=$(find dist/ -name "*.whl" | head -n 1)
    if [[ -z "$WHEEL_FILE" ]]; then
        print_error "Failed to build wheel file"
        exit 1
    fi
    
    print_info "Installing ipip from wheel: $WHEEL_FILE"
    $PYTHON_CMD -m pip install "$WHEEL_FILE" --force-reinstall
    
elif [[ -f "setup.py" ]]; then
    # Legacy build
    print_info "Installing ipip from setup.py..."
    $PYTHON_CMD -m pip install . --force-reinstall
else
    print_error "No pyproject.toml or setup.py found. Are you in the ipip directory?"
    exit 1
fi

# Verify installation
print_info "Verifying installation..."
if command -v ipip &> /dev/null; then
    print_success "ipip successfully installed!"
    echo
    print_info "Testing basic functionality..."
    ipip --help > /dev/null
    print_success "ipip is working correctly!"
    echo
    print_info "🎉 Installation complete!"
    echo
    print_info "Running first-time setup..."
    $PYTHON_CMD -c "from ipip.ollama_installer import OllamaInstaller; OllamaInstaller(verbose=True).interactive_setup()"
    
    echo
    print_info "Try these commands:"
    echo "  ipip blender --dry-run"
    echo "  ipip 'computer vision' --dry-run"
    echo "  ipip --verbose 'build a chatbot' --dry-run"
    echo "  ipip 'move test files to tests folder' --dry-run"
    
else
    print_error "Installation failed. ipip command not found."
    print_info "Try adding ~/.local/bin to your PATH:"
    echo "  export PATH=\"\$HOME/.local/bin:\$PATH\""
    exit 1
fi