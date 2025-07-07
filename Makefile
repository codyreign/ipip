# Makefile for ipip - Intelligent pip package installer
# Provides easy commands for building, installing, and managing ipip

.PHONY: help install install-dev build clean test lint format uninstall check-deps

# Default target
help:
	@echo "🚀 ipip - Intelligent pip package installer"
	@echo ""
	@echo "Available commands:"
	@echo "  make install      - Install ipip system-wide"
	@echo "  make install-dev  - Install in development mode"
	@echo "  make build        - Build package (wheel + sdist)"
	@echo "  make clean        - Clean build artifacts"
	@echo "  make test         - Run tests"
	@echo "  make lint         - Run linting"
	@echo "  make format       - Format code"
	@echo "  make uninstall    - Uninstall ipip"
	@echo "  make check-deps   - Check dependencies"
	@echo ""
	@echo "Quick start:"
	@echo "  git clone <repo>"
	@echo "  cd ipip"
	@echo "  make install"

# Install ipip system-wide
install: check-deps build
	@echo "📦 Installing ipip system-wide..."
	pip install 'click>=8.0.0' 'requests>=2.25.0' 'rich>=10.0.0' 'packaging>=21.0'
	pip install dist/*.whl --force-reinstall
	@echo "✅ Installation complete!"
	@echo ""
	@echo "Try: ipip blender --dry-run"

# Install in development mode (editable)
install-dev: check-deps
	@echo "🔧 Installing ipip in development mode..."
	pip install 'click>=8.0.0' 'requests>=2.25.0' 'rich>=10.0.0' 'packaging>=21.0'
	pip install -e . --force-reinstall
	@echo "✅ Development installation complete!"
	@echo ""
	@echo "Changes to source code will take effect immediately."

# Build package
build: clean
	@echo "🏗️  Building ipip package..."
	python -m pip install build
	python -m build
	@echo "✅ Build complete! Files in dist/"

# Clean build artifacts
clean:
	@echo "🧹 Cleaning build artifacts..."
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
	@echo "✅ Cleanup complete!"

# Run tests
test: check-deps
	@echo "🧪 Running tests..."
	python -m pytest tests/ -v --tb=short
	@echo "✅ Tests complete!"

# Run linting
lint: check-deps
	@echo "🔍 Running linting..."
	python -m flake8 ipip/ --max-line-length=100
	python -m pylint ipip/ || true
	@echo "✅ Linting complete!"

# Format code
format: check-deps
	@echo "✨ Formatting code..."
	python -m black ipip/ --line-length=100
	python -m isort ipip/ --profile black
	@echo "✅ Formatting complete!"

# Uninstall ipip
uninstall:
	@echo "🗑️  Uninstalling ipip..."
	pip uninstall ipip -y || true
	@echo "✅ Uninstall complete!"

# Check dependencies
check-deps:
	@echo "🔍 Checking dependencies..."
	@python --version || (echo "❌ Python not found" && exit 1)
	@python -m pip --version || (echo "❌ pip not found" && exit 1)
	@echo "✅ Dependencies OK!"

# Development setup
dev-setup: install-dev
	@echo "🔧 Setting up development environment..."
	pip install pytest flake8 black isort pylint
	@echo "✅ Development environment ready!"

# Build and test everything
all: clean lint test build
	@echo "🎉 All tasks completed successfully!"

# Install from GitHub (for users)
install-github:
	@echo "📥 Installing ipip from GitHub..."
	pip install git+https://github.com/yourusername/ipip.git
	@echo "✅ GitHub installation complete!"