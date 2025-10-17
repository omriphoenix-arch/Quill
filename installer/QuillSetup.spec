# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec file for Quill GUI Installer

block_cipher = None

a = Analysis(
    ['setup_gui.py'],
    pathex=[],
    binaries=[],
    datas=[
        # Project root files
        ('../LICENSE', '.'),
        ('../README.md', '.'),
        ('../CHANGELOG.md', '.'),
        ('../requirements.txt', '.'),
        
        # Core interpreter (CRITICAL!)
        ('../core', 'core'),
        
        # Examples
        ('../examples', 'examples'),
        
        # Games
        ('../games', 'games'),
        
        # Documentation
        ('../documentation', 'documentation'),
        ('../docs', 'docs'),
        
        # Resources (icons, etc.)
        ('../resources', 'resources'),
        
        # Scripts and batch files
        ('../scripts', 'scripts'),
        ('../quill.bat', '.'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='QuillSetup-1.0.2',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Windowed application (no console)
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='../resources/icons/quill_icon.ico',
    version_file=None,
)
