# main.spec

# Import necessary modules
# Ensure you have the required imports at the top
from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import collect_submodules

# Define your analysis configuration
a = Analysis(
    ['main.py'],  # Main script to analyze
    pathex=['/home/kali/gamedata'],  # Adjust this path as needed
    binaries=[],
    datas=[('sounds/*', 'sounds')],  # Include sound and assets
    hiddenimports=collect_submodules('pygame'),  # Collect hidden imports (e.g., pygame)
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

# PyInstaller's pyz and EXE generation
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,  # Ensure assets and sounds are included here
    [],
    name='main',  # Name of the executable
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,  # Disabled UPX for Linux (you can enable it for Windows)
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Set to True if you want a console window on Linux
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
