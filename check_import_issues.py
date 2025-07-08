#!/usr/bin/env python3
"""
Check for import issues that might cause build to hang.
"""

import sys
import importlib
import traceback
from pathlib import Path

def test_individual_imports():
    """Test importing each module individually."""
    print("🔍 Testing Individual Module Imports")
    print("=" * 50)
    
    # Add current directory to path
    sys.path.insert(0, str(Path.cwd()))
    
    modules_to_test = [
        "ipip",
        "ipip.cli",
        "ipip.config", 
        "ipip.llm_resolver",
        "ipip.package_installer",
        "ipip.package_searcher",
        "ipip.requirements_manager",
        "ipip.file_analyzer",
        "ipip.file_operations",
        "ipip.file_context",
        "ipip.emergency_undo",
        "ipip.ollama_installer"
    ]
    
    failed_imports = []
    
    for module_name in modules_to_test:
        try:
            print(f"Testing: {module_name}...", end=" ")
            module = importlib.import_module(module_name)
            print("✅ OK")
        except Exception as e:
            print(f"❌ FAILED: {e}")
            failed_imports.append((module_name, str(e)))
    
    if failed_imports:
        print(f"\n⚠️ {len(failed_imports)} import failures detected:")
        for module, error in failed_imports:
            print(f"   {module}: {error}")
        return False
    else:
        print("\n✅ All imports successful!")
        return True

def test_cli_import():
    """Test CLI import specifically (often causes issues)."""
    print("\n🖥️ Testing CLI Import")
    print("=" * 50)
    
    try:
        from ipip.cli import main
        print("✅ CLI main function imported successfully")
        
        # Test if Click is working
        import click
        print(f"✅ Click version: {click.__version__}")
        
        return True
    except Exception as e:
        print(f"❌ CLI import failed: {e}")
        traceback.print_exc()
        return False

def test_entry_points():
    """Test entry points that might cause build issues."""
    print("\n🚪 Testing Entry Points")
    print("=" * 50)
    
    try:
        # Test if the entry point can be resolved
        from ipip.cli import main
        print("✅ Entry point 'ipip.cli:main' can be resolved")
        
        # Test CLI help (without actually running)
        import click
        from click.testing import CliRunner
        
        runner = CliRunner()
        # This imports the CLI but doesn't run it
        print("✅ CLI can be instantiated for testing")
        
        return True
    except Exception as e:
        print(f"❌ Entry point test failed: {e}")
        traceback.print_exc()
        return False

def test_dependency_resolution():
    """Test if dependencies can be resolved."""
    print("\n📦 Testing Dependencies")
    print("=" * 50)
    
    required_deps = [
        "click",
        "requests", 
        "rich",
        "packaging"
    ]
    
    missing_deps = []
    
    for dep in required_deps:
        try:
            module = importlib.import_module(dep)
            version = getattr(module, "__version__", "unknown")
            print(f"✅ {dep}: {version}")
        except ImportError:
            print(f"❌ {dep}: Missing")
            missing_deps.append(dep)
    
    if missing_deps:
        print(f"\n⚠️ Missing dependencies: {missing_deps}")
        return False
    else:
        print("\n✅ All dependencies available!")
        return True

def test_circular_imports():
    """Test for circular imports that might cause hangs."""
    print("\n🔄 Testing for Circular Imports")
    print("=" * 50)
    
    try:
        # Clear module cache
        modules_to_clear = [name for name in sys.modules.keys() if name.startswith('ipip')]
        for module_name in modules_to_clear:
            del sys.modules[module_name]
        
        # Try importing everything at once
        import ipip
        from ipip import cli, config, llm_resolver, file_operations
        
        print("✅ No circular import issues detected")
        return True
    except Exception as e:
        print(f"❌ Circular import or other issue: {e}")
        traceback.print_exc()
        return False

def test_build_time_imports():
    """Test imports that happen during build time."""
    print("\n⚙️ Testing Build-Time Imports")  
    print("=" * 50)
    
    try:
        # Test setuptools discovery
        import setuptools
        print(f"✅ setuptools: {setuptools.__version__}")
        
        # Test if our package can be discovered
        from setuptools import find_packages
        packages = find_packages()
        print(f"✅ Discovered packages: {packages}")
        
        # Test entry point discovery
        if Path("pyproject.toml").exists():
            try:
                import tomllib
                with open("pyproject.toml", "rb") as f:
                    config = tomllib.load(f)
                print("✅ pyproject.toml can be parsed")
                
                if "project" in config and "scripts" in config["project"]:
                    scripts = config["project"]["scripts"]
                    print(f"✅ Entry points found: {scripts}")
            except ImportError:
                # Try tomli for older Python
                try:
                    import tomli
                    with open("pyproject.toml", "rb") as f:
                        config = tomli.load(f)
                    print("✅ pyproject.toml parsed with tomli")
                except ImportError:
                    print("⚠️ No TOML parser available (install tomli)")
        
        return True
    except Exception as e:
        print(f"❌ Build-time import issue: {e}")
        traceback.print_exc()
        return False

def main():
    """Run all import tests."""
    print("🧪 Import Issues Diagnostic")
    print("=" * 60)
    
    tests = [
        ("Individual Imports", test_individual_imports),
        ("CLI Import", test_cli_import),
        ("Entry Points", test_entry_points),
        ("Dependencies", test_dependency_resolution),
        ("Circular Imports", test_circular_imports),
        ("Build-Time Imports", test_build_time_imports)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"💥 {test_name} crashed: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n📊 Test Results")
    print("=" * 50)
    
    passed = 0
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{status}: {test_name}")
        if result:
            passed += 1
    
    print(f"\n🎯 {passed}/{len(results)} tests passed")
    
    if passed == len(results):
        print("✅ No import issues detected - build hanging is likely due to other causes")
        print("💡 Try: python debug_build_verbose.py")
    else:
        print("⚠️ Import issues detected - fix these before building")
    
    return passed == len(results)

if __name__ == "__main__":
    main()