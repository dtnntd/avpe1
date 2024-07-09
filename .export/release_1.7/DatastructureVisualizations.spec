# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['..\\DatastructureVisualizations.py'],
    pathex=[],
    binaries=[],
    datas=[('D:\\DTN\\OneDrive - 0z6pk\\Study_Hnue\\2023-2024\\kl\\datastructures-visualization\\PythonVisualizations\\*.png', '.'), ('C:/Program Files (x86)/Windows Kits/10/Redist/10.0.26100.0/ucrt/DLLs/x86/*.dll', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='DatastructureVisualizations',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['D:\\DTN\\OneDrive - 0z6pk\\Study_Hnue\\2023-2024\\kl\\datastructures-visualization\\PythonVisualizations\\design\\Datastructure-Visualizations-icon.ico'],
)
