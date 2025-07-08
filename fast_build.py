#!/usr/bin/env python3
"""
Fast build script that bypasses python -m build to avoid hanging.
"""

import subprocess
import sys
import os
import shutil
from pathlib import Path

def find_python():
    """Find working Python command."""
    for cmd in ["py", "python3", "python"]:
        try:
            result = subprocess.run([cmd, "--version"], capture_output=True, timeout=5)
            if result.returncode == 0:
                # Test if it's real Python
                test = subprocess.run([cmd, "-c", "import sys"], capture_output=True, timeout=5)
                if test.returncode == 0:
                    return cmd
        except:
            continue
    return None

def run_cmd(cmd, description):
    """Run command with real-time output."""
    print(f"🔄 {description}")
    print(f"   Running: {cmd}")
    
    try:
        result = subprocess.run(cmd, shell=True, check=True)
        print(f"✅ {description} - Success")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - Failed (exit code: {e.returncode})")
        return False

def simple_build():
    """Build using simple pip wheel approach."""
    print("🔨 Simple Build Process")
    print("=" * 50)
    
    python_cmd = find_python()
    if not python_cmd:
        print("❌ No Python found")
        return False
    
    print(f"✅ Using Python: {python_cmd}")
    
    # Clean
    print("\n1️⃣ Cleaning...")
    for path in ["build", "dist"]:
        if Path(path).exists():
            shutil.rmtree(path)
            print(f"   Removed: {path}/")
    
    # Create dist directory
    Path("dist").mkdir(exist_ok=True)
    
    # Method 1: pip wheel (fastest, no isolation issues)
    print("\n2️⃣ Building wheel with pip...")
    success = run_cmd(f"{python_cmd} -m pip wheel . --no-deps --wheel-dir dist", "Building wheel")
    
    if success:
        # Method 2: Create source distribution manually
        print("\n3️⃣ Creating source distribution...")
        success = run_cmd(f"{python_cmd} -c \"import setuptools; setuptools.setup()\" sdist --dist-dir dist", "Creating source dist")
        
        if not success:
            # Alternative: use build for sdist only
            print("   Trying alternative source build...")
            success = run_cmd(f"{python_cmd} -m build --sdist --outdir dist", "Building source (alternative)")
    
    # Check results
    if Path("dist").exists():
        files = list(Path("dist").glob("*"))
        if files:
            print(f"\n✅ Build successful! Generated {len(files)} files:")
            for f in files:
                size = f.stat().st_size
                size_str = f"{size//1024}KB" if size > 1024 else f"{size}B"
                print(f"   📦 {f.name} ({size_str})")
            return True
    
    print("\n❌ Build failed - no files generated")
    return False

def setup_py_build():
    """Fallback: create temporary setup.py and use it."""
    print("\n🔧 Fallback: setup.py build")
    print("=" * 50)
    
    python_cmd = find_python()
    if not python_cmd:
        return False
    
    # Create minimal setup.py
    setup_content = '''
from setuptools import setup, find_packages

# Try to import tomllib (Python 3.11+) or tomli
try:
    import tomllib
except ImportError:
    import tomli as tomllib

# Read pyproject.toml
with open("pyproject.toml", "rb") as f:
    config = tomllib.load(f)

project = config["project"]

setup(
    name=project["name"],
    version=project["version"],
    description=project["description"],
    author=project["authors"][0]["name"],
    author_email=project["authors"][0]["email"],
    packages=find_packages(),
    install_requires=project["dependencies"],
    entry_points={
        "console_scripts": [
            "ipip = ipip.cli:main"
        ]
    },
    python_requires=project["requires-python"],
    classifiers=project["classifiers"],
)
'''
    
    print("📝 Creating temporary setup.py...")
    with open("setup.py", "w") as f:
        f.write(setup_content)
    
    try:
        # Build with setup.py
        success1 = run_cmd(f"{python_cmd} setup.py bdist_wheel", "Building wheel with setup.py")
        success2 = run_cmd(f"{python_cmd} setup.py sdist", "Building source with setup.py")
        
        return success1 or success2
    finally:
        # Clean up
        if Path("setup.py").exists():
            Path("setup.py").unlink()
            print("🧹 Cleaned up temporary setup.py")

def main():
    """Try multiple build approaches."""
    print("⚡ Fast Build (Bypass Hanging Issues)")
    print("=" * 60)
    
    # Check requirements
    if not Path("pyproject.toml").exists():
        print("❌ No pyproject.toml found")
        return 1
    
    # Try simple build first
    if simple_build():
        print("\n🎉 Simple build successful!")
        return 0
    
    print("\n🔄 Simple build failed, trying setup.py approach...")
    
    # Try setup.py fallback
    try:
        import tomllib
    except ImportError:
        try:
            import tomli as tomllib
        except ImportError:
            print("❌ No TOML parser available (need tomli for Python < 3.11)")
            return 1
    
    if setup_py_build():
        print("\n🎉 Setup.py build successful!")
        return 0
    
    print("\n💥 All build methods failed")
    print("🔍 Try running: python check_import_issues.py")
    print("🔍 Or run: python debug_build_verbose.py")
    return 1

if __name__ == "__main__":
    sys.exit(main())