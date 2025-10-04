"""
Environment Verification Script
Checks if all required packages are installed correctly
"""

import sys

def check_package(package_name):
    """Check if a package is installed"""
    try:
        __import__(package_name)
        print(f"✅ {package_name:<25} - Installed")
        return True
    except ImportError:
        print(f"❌ {package_name:<25} - NOT Installed")
        return False

def main():
    print("=" * 60)
    print("NeuroGrid ScriptSense - Environment Check")
    print("=" * 60)
    print()
    
    # Check Python version
    print(f"Python Version: {sys.version}")
    print()
    
    # List of required packages
    packages = [
        'streamlit',
        'gradient',
        'gtts',
        'pandas',
        'numpy',
        'PIL',  # Pillow
        'requests',
    ]
    
    print("Checking Required Packages:")
    print("-" * 60)
    
    all_installed = True
    for package in packages:
        if not check_package(package):
            all_installed = False
    
    print()
    print("=" * 60)
    
    if all_installed:
        print("✅ All required packages are installed!")
        print()
        print("You can now run the application with:")
        print("  streamlit run main.py")
        print()
        print("Or use the helper scripts:")
        print("  run_app.bat  (Windows Batch)")
        print("  .\\run_app.ps1  (PowerShell)")
    else:
        print("❌ Some packages are missing!")
        print()
        print("Please install missing packages with:")
        print("  pip install -r requirements.txt")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
