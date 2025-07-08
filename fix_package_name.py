#!/usr/bin/env python3
"""
Fix package name consistency between pyproject.toml and entry points.
"""

from pathlib import Path

def check_package_name_consistency():
    """Check if package name is consistent across files."""
    print("🔍 Checking package name consistency")
    print("=" * 40)
    
    # Read pyproject.toml
    pyproject_path = Path("pyproject.toml")
    if not pyproject_path.exists():
        print("❌ pyproject.toml not found")
        return False
    
    content = pyproject_path.read_text()
    
    # Extract package name
    package_name = None
    for line in content.split('\n'):
        if line.startswith('name = '):
            package_name = line.split('=')[1].strip().strip('"\'')
            break
    
    if not package_name:
        print("❌ Could not find package name in pyproject.toml")
        return False
    
    print(f"📦 Package name in pyproject.toml: {package_name}")
    
    # Check entry point
    if "ipip = \"ipip.cli:main\"" in content:
        if package_name == "inpip":
            print("⚠️ Package name is 'inpip' but entry point references 'ipip' module")
            print("💡 This will cause import errors")
            return False
        else:
            print("✅ Entry point matches package structure")
    
    # Check if directory structure matches
    if package_name == "inpip" and Path("ipip").exists():
        print("⚠️ Package name is 'inpip' but directory is 'ipip/'")
        print("💡 Consider renaming directory or changing package name back")
        return False
    
    if package_name == "ipip" and Path("ipip").exists():
        print("✅ Package name and directory structure match")
        return True
    
    return True

def suggest_fix():
    """Suggest how to fix the package name issue."""
    print("\n🔧 Suggested Fix")
    print("=" * 40)
    
    print("Option 1: Keep 'ipip' everywhere (recommended)")
    print("  - Change package name back to 'ipip' in pyproject.toml")
    print("  - Keep existing 'ipip/' directory")
    print("  - Keep existing entry point")
    
    print("\nOption 2: Change everything to 'inpip'")
    print("  - Rename 'ipip/' directory to 'inpip/'")
    print("  - Update entry point to 'inpip.cli:main'")
    print("  - Update all import statements")
    
    print("\n💡 Option 1 is much easier and recommended!")

def quick_fix_to_ipip():
    """Quick fix: change package name back to 'ipip'."""
    pyproject_path = Path("pyproject.toml")
    if not pyproject_path.exists():
        return False
    
    content = pyproject_path.read_text()
    
    # Replace inpip with ipip
    if 'name = "inpip"' in content:
        new_content = content.replace('name = "inpip"', 'name = "ipip"')
        pyproject_path.write_text(new_content)
        print("✅ Fixed: Changed package name back to 'ipip' in pyproject.toml")
        return True
    
    return False

def main():
    """Check and optionally fix package name issues."""
    print("🔧 Package Name Consistency Checker")
    print("=" * 50)
    
    if check_package_name_consistency():
        print("✅ Package name is consistent")
        return 0
    
    suggest_fix()
    
    response = input("\n❓ Apply quick fix (change package name back to 'ipip')? (y/N): ")
    
    if response.lower() == 'y':
        if quick_fix_to_ipip():
            print("🎉 Fixed! Now try running 'ipip install requirements' again")
            return 0
        else:
            print("❌ Could not apply fix")
            return 1
    else:
        print("💡 Please fix the package name manually")
        return 1

if __name__ == "__main__":
    exit(main())