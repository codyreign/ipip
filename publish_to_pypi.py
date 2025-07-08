#!/usr/bin/env python3
"""
Script to publish ipip to PyPI
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def run_command(cmd, description=""):
    """Run a command and handle errors"""
    print(f"\n🔄 {description}")
    print(f"Running: {cmd}")
    
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"❌ Error: {result.stderr}")
        return False
    
    print(f"✅ Success: {result.stdout}")
    return True

def check_tools():
    """Check if required tools are installed"""
    tools = ['twine', 'build']
    missing = []
    
    for tool in tools:
        result = subprocess.run(f"python -m {tool} --version", shell=True, capture_output=True)
        if result.returncode != 0:
            missing.append(tool)
    
    if missing:
        print(f"❌ Missing tools: {', '.join(missing)}")
        print("Install with: pip install --upgrade pip setuptools wheel twine build")
        return False
    
    return True

def clean_build():
    """Clean previous build artifacts"""
    print("\n🧹 Cleaning previous builds...")
    
    paths_to_clean = ['dist', 'build', 'ipip.egg-info']
    
    for path in paths_to_clean:
        if os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)
            print(f"  Removed: {path}")

def build_package():
    """Build the package"""
    # Use fast pip wheel method
    success1 = run_command("python -m pip wheel . --no-deps --wheel-dir dist", "Building wheel with pip")
    if not success1:
        print("Wheel build failed, trying alternative...")
        success1 = run_command("python -m build --wheel --no-isolation", "Building wheel (no isolation)")
    
    # Build source distribution
    success2 = run_command("python -m build --sdist --outdir dist", "Building source distribution")
    if not success2:
        print("Source build failed, trying alternative...")
        success2 = run_command("python setup.py sdist --dist-dir dist", "Building source (setuptools)")
    
    return success1 or success2  # At least one should succeed

def upload_to_testpypi():
    """Upload to TestPyPI"""
    return run_command("twine upload --repository testpypi dist/*", "Uploading to TestPyPI")

def upload_to_pypi():
    """Upload to PyPI"""
    return run_command("twine upload dist/*", "Uploading to PyPI")

def main():
    print("🚀 Publishing ipip to PyPI")
    print("=" * 50)
    
    # Check current directory
    if not Path("pyproject.toml").exists():
        print("❌ Error: pyproject.toml not found. Run this script from the project root.")
        sys.exit(1)
    
    # Check tools
    if not check_tools():
        sys.exit(1)
    
    # Clean previous builds
    clean_build()
    
    # Build package
    if not build_package():
        print("❌ Build failed!")
        sys.exit(1)
    
    # Ask user what to do
    print("\n📋 What would you like to do?")
    print("1. Upload to TestPyPI (recommended first)")
    print("2. Upload to PyPI (production)")
    print("3. Both (TestPyPI then PyPI)")
    print("4. Exit")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice == "1":
        if upload_to_testpypi():
            print("\n🎉 Successfully uploaded to TestPyPI!")
            print("Test with: pip install --index-url https://test.pypi.org/simple/ ipip")
    
    elif choice == "2":
        confirm = input("\n⚠️  Are you sure you want to upload to PyPI? This cannot be undone. (y/N): ")
        if confirm.lower() == 'y':
            if upload_to_pypi():
                print("\n🎉 Successfully uploaded to PyPI!")
                print("Install with: pip install ipip")
        else:
            print("Upload cancelled.")
    
    elif choice == "3":
        if upload_to_testpypi():
            print("\n✅ TestPyPI upload successful!")
            confirm = input("\nContinue with PyPI upload? (y/N): ")
            if confirm.lower() == 'y':
                if upload_to_pypi():
                    print("\n🎉 Successfully uploaded to PyPI!")
                    print("Install with: pip install ipip")
        else:
            print("❌ TestPyPI upload failed. Stopping.")
    
    elif choice == "4":
        print("👋 Goodbye!")
    
    else:
        print("❌ Invalid choice.")
        sys.exit(1)

if __name__ == "__main__":
    main()