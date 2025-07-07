#!/usr/bin/env python3
"""
Build script for ipip package.
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(cmd, description, show_output=False):
    """Run a command and handle errors."""
    print(f"BUILDING: {description}...")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        print(f"SUCCESS: {description} completed successfully")
        if show_output and result.stdout:
            print(f"   Output: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"ERROR: {description} failed")
        if e.stdout:
            print(f"   Output: {e.stdout.strip()}")
        if e.stderr:
            print(f"   Error: {e.stderr.strip()}")
        return False

def main():
    """Main build process."""
    print("BUILD: Building ipip package for PyPI...\n")
    
    # Check if we're in the right directory
    if not Path("pyproject.toml").exists():
        print("ERROR: pyproject.toml not found. Please run from the project root.")
        return 1
    
    # Clean previous builds
    print("CLEAN: Cleaning previous builds...")
    import shutil
    for dir_name in ["build", "dist"]:
        if Path(dir_name).exists():
            shutil.rmtree(dir_name)
    
    # Clean egg-info directories
    for egg_info in Path(".").glob("*.egg-info"):
        if egg_info.exists():
            shutil.rmtree(egg_info)
    
    # Detect Python command
    python_cmd = "python3"  # Default
    try:
        subprocess.run(["python3", "--version"], capture_output=True, check=True)
        python_cmd = "python3"
    except (subprocess.CalledProcessError, FileNotFoundError):
        try:
            subprocess.run(["python", "--version"], capture_output=True, check=True)
            python_cmd = "python"
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("ERROR: Neither 'python' nor 'python3' command found!")
            return 1
    
    print(f"PYTHON: Using {python_cmd}")
    
    # Install build dependencies
    print("DEPS: Installing build dependencies...")
    build_deps = ["build", "twine", "wheel"]
    
    for dep in build_deps:
        check_cmd = f"{python_cmd} -m pip show {dep}"
        if not run_command(f"{check_cmd} >nul 2>&1" if os.name == 'nt' else f"{check_cmd} >/dev/null 2>&1", f"Checking {dep}"):
            run_command(f"{python_cmd} -m pip install {dep}", f"Installing {dep}")
    
    # Run minimal tests (no external dependencies required)
    print("\nTEST: Running minimal tests...")
    test_result = run_command(f"{python_cmd} minimal_test.py", "Minimal functionality tests", show_output=True)
    if not test_result:
        print("ERROR: Tests failed. Please fix issues before building.")
        return 1
    
    # Build the package
    print("\nBUILD: Building package...")
    if not run_command(f"{python_cmd} -m build", "Building wheel and source distribution"):
        return 1
    
    # Check the built package
    print("\nCHECK: Checking built package...")
    if not run_command(f"{python_cmd} -m twine check dist/*", "Checking package integrity"):
        return 1
    
    # List built files
    print("\nFILES: Built files:")
    dist_files = list(Path("dist").glob("*"))
    for file_path in dist_files:
        print(f"   {file_path}")
    
    print("\nSUCCESS: Build completed successfully!")
    print("\nNEXT: Next steps:")
    print("   1. Test the package locally:")
    print(f"      {python_cmd} -m pip install dist/ipip-*.whl")
    print("   2. Upload to TestPyPI:")
    print(f"      {python_cmd} -m twine upload --repository testpypi dist/*")
    print("   3. Upload to PyPI:")
    print(f"      {python_cmd} -m twine upload dist/*")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())