#!/bin/bash
# ipip uninstaller for Unix/Linux/macOS

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_info() { echo -e "${BLUE}[INFO]${NC} $1"; }
print_success() { echo -e "${GREEN}[SUCCESS]${NC} $1"; }
print_warning() { echo -e "${YELLOW}[WARNING]${NC} $1"; }
print_error() { echo -e "${RED}[ERROR]${NC} $1"; }

print_info "🗑️  Uninstalling ipip..."
echo

# Determine Python command
PYTHON_CMD="python3"
if ! command -v python3 &> /dev/null; then
    PYTHON_CMD="python"
fi

# Check if ipip is installed
if ! command -v ipip &> /dev/null; then
    print_warning "ipip is not installed or not in PATH"
else
    print_info "Found ipip installation"
fi

# Uninstall using pip
print_info "Removing ipip package..."
$PYTHON_CMD -m pip uninstall ipip -y

# Verify uninstallation
if command -v ipip &> /dev/null; then
    print_warning "ipip command still found in PATH"
    print_info "You may need to restart your terminal or check your PATH"
else
    print_success "ipip successfully uninstalled!"
fi

print_info "✅ Uninstallation complete!"
echo
print_info "Thank you for using ipip! 👋"