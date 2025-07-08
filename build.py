#!/usr/bin/env python3
"""
Build script for ipip package.
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(cmd, description, show_output=False, show_progress=False):
    """Run a command and handle errors."""
    print(f"BUILDING: {description}...")
    try:
        if show_progress:
            # Show real-time output for long-running commands
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, 
                                     stderr=subprocess.STDOUT, text=True, 
                                     universal_newlines=True, bufsize=1)
            
            output_lines = []
            for line in process.stdout:
                line = line.rstrip()
                if line:
                    print(f"   {line}")
                    output_lines.append(line)
            
            process.wait()
            
            if process.returncode == 0:
                print(f"SUCCESS: {description} completed successfully")
                return True
            else:
                print(f"ERROR: {description} failed with exit code {process.returncode}")
                return False
        else:
            # Standard capture mode for quick commands
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
    except KeyboardInterrupt:
        print(f"\nINTERRUPTED: {description} was cancelled by user")
        return False

def main():
    """Main build process."""
    print("BUILD: Building ipip package for PyPI...\n")
    
    # Check if we're in the right directory
    if not Path("pyproject.toml").exists():
        print("ERROR: pyproject.toml not found. Please run from the project root.")
        return 1
    
    # Check for required files
    required_files = ["README.md", "ipip/__init__.py", "ipip/cli.py"]
    for file_path in required_files:
        if not Path(file_path).exists():
            print(f"ERROR: Required file {file_path} not found")
            return 1
    
    print("VERIFY: All required files found")
    
    # Clean previous builds
    print("CLEAN: Cleaning previous builds...")
    import shutil
    for dir_name in ["build", "dist"]:
        if Path(dir_name).exists():
            shutil.rmtree(dir_name)
            print(f"   Removed: {dir_name}/")
    
    # Clean egg-info directories
    for egg_info in Path(".").glob("*.egg-info"):
        if egg_info.exists():
            shutil.rmtree(egg_info)
            print(f"   Removed: {egg_info.name}/")
    
    # Detect Python command (robust Windows-compatible detection)
    python_cmd = None
    python_version = None
    
    print("PYTHON: Looking for Python installation...")
    
    # Try different Python commands in order of preference
    python_candidates = ["py", "python3", "python"]
    
    for cmd in python_candidates:
        try:
            result = subprocess.run([cmd, "--version"], capture_output=True, check=True, text=True)
            version_output = result.stdout.strip()
            
            # For 'python' command, check if it's the real Python or Microsoft Store stub
            if cmd == "python":
                try:
                    subprocess.run([cmd, "-c", "import sys; print('real')"], 
                                 capture_output=True, check=True, timeout=5)
                except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
                    print(f"PYTHON: {cmd} appears to be Microsoft Store stub, skipping...")
                    continue
            
            python_cmd = cmd
            python_version = version_output.split()[1] if len(version_output.split()) > 1 else "unknown"
            break
            
        except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
            continue
    
    if not python_cmd:
        print("ERROR: No accessible Python installation found!")
        print("HELP: Please install Python 3.8+ from https://python.org")
        print("HELP: Make sure to check 'Add Python to PATH' during installation")
        print("HELP: Or try running as administrator")
        print("HELP: You can also try using the Python Launcher: py --version")
        return 1
    
    print(f"PYTHON: Using {python_cmd} (Python {python_version})")
    
    # Check Python version is 3.8+
    try:
        version_parts = python_version.split('.')
        major = int(version_parts[0])
        minor = int(version_parts[1]) if len(version_parts) > 1 else 0
        
        if major < 3 or (major == 3 and minor < 8):
            print(f"ERROR: Python 3.8+ is required. Found: {python_version}")
            return 1
            
    except (ValueError, IndexError):
        print(f"WARNING: Could not parse Python version: {python_version}")
        print("Continuing anyway...")
    
    # Install build dependencies
    print("DEPS: Installing build dependencies...")
    build_deps = ["build", "twine", "wheel"]
    
    for dep in build_deps:
        check_cmd = f"{python_cmd} -m pip show {dep}"
        if not run_command(f"{check_cmd} >nul 2>&1" if os.name == 'nt' else f"{check_cmd} >/dev/null 2>&1", f"Checking {dep}"):
            run_command(f"{python_cmd} -m pip install {dep}", f"Installing {dep}")
    
    # Run minimal tests (no external dependencies required)
    print("\nTEST: Running minimal tests...")
    if Path("minimal_test.py").exists():
        test_result = run_command(f"{python_cmd} minimal_test.py", "Minimal functionality tests", show_output=True)
        if not test_result:
            print("ERROR: Tests failed. Please fix issues before building.")
            return 1
    else:
        print("INFO: No minimal_test.py found, skipping minimal tests")
    
    # Build the package
    print("\nBUILD: Building package...")
    print("   Using fast pip wheel method (bypasses hanging issues)...")
    
    # Create dist directory
    Path("dist").mkdir(exist_ok=True)
    
    # Build wheel with pip (fast method that works)
    if not run_command(f"{python_cmd} -m pip wheel . --no-deps --wheel-dir dist", "Building wheel with pip"):
        print("   Wheel build failed, trying alternative method...")
        # Fallback to build without isolation
        if not run_command(f"{python_cmd} -m build --wheel --no-isolation", "Building wheel (no isolation)", show_progress=True):
            return 1
    
    # Build source distribution
    if not run_command(f"{python_cmd} -m build --sdist --outdir dist", "Building source distribution"):
        print("   Source build failed, trying alternative...")
        # Try manual sdist
        if not run_command(f"{python_cmd} setup.py sdist --dist-dir dist", "Building source (setuptools)"):
            print("   WARNING: Source distribution build failed, continuing with wheel only...")
    
    print("   Build method: pip wheel + build sdist (faster, more reliable)")
    
    # Check if build produced files
    dist_path = Path("dist")
    if not dist_path.exists():
        print("ERROR: Build failed - no dist directory created")
        return 1
    
    wheel_files = list(dist_path.glob("*.whl"))
    source_files = list(dist_path.glob("*.tar.gz"))
    
    if not wheel_files:
        print("ERROR: No wheel file created")
        return 1
    
    if not source_files:
        print("ERROR: No source distribution created")
        return 1
    
    # Check the built package
    print("\nCHECK: Checking built package...")
    if not run_command(f"{python_cmd} -m twine check dist/*", "Checking package integrity"):
        print("WARNING: Package check failed, but continuing...")
    
    # List built files
    print("\nFILES: Built files:")
    dist_files = list(Path("dist").glob("*"))
    for file_path in dist_files:
        size = file_path.stat().st_size
        size_str = f"{size // 1024}KB" if size > 1024 else f"{size}B"
        print(f"   {file_path.name} ({size_str})")
    
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