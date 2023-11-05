# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['calculator.py'],
    pathex=[],
    binaries=[],
    datas=[('../Calculator_with_kivy/calculator.kv', '.')],
    hiddenimports=['kivy_deps.sdl2', 'kivy_deps.glew'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)


exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='calculator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    Tree('../Calculator_with_kivy'),
    a.binaries,
    a.datas,
    #*[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    strip=False,
    upx=True,
    upx_exclude=[],
    name='calculator',
)
