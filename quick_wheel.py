#!/usr/bin/env python3
"""
Quick wheel build using pip wheel method (usually works when build hangs).
"""

import subprocess
import sys
from pathlib import Path

def quick_build():
    """Quick build using pip wheel."""
    print("⚡ Quick Wheel Build")
    print("=" * 30)
    
    # Find Python
    python_cmd = None
    for cmd in ["py", "python3", "python"]:
        try:
            result = subprocess.run([cmd, "--version"], capture_output=True, timeout=5)
            if result.returncode == 0:
                python_cmd = cmd
                break
        except:
            continue
    
    if not python_cmd:
        print("❌ No Python found")
        return False
    
    print(f"Using: {python_cmd}")
    
    # Clean
    for path in ["build", "dist"]:
        if Path(path).exists():
            import shutil
            shutil.rmtree(path)
    
    Path("dist").mkdir(exist_ok=True)
    
    # Build wheel with pip (fast method)
    print("\n🔄 Building wheel...")
    try:
        result = subprocess.run([
            python_cmd, "-m", "pip", "wheel", ".", 
            "--no-deps", "--wheel-dir", "dist"
        ], check=True, text=True)
        
        print("✅ Wheel build successful!")
        
        # Check result
        wheels = list(Path("dist").glob("*.whl"))
        if wheels:
            for wheel in wheels:
                print(f"📦 {wheel.name}")
            return True
        else:
            print("❌ No wheel file created")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        return False

if __name__ == "__main__":
    if quick_build():
        print("\n🎉 Quick build successful!")
        print("You can upload this wheel to PyPI")
    else:
        print("\n💥 Quick build failed")