block_cipher = None

a = Analysis(
    ['src/pomodoro.py'],
    pathex=[],
    binaries=[],
    datas=[('src/complete.mp3', '.')],
    hiddenimports=['rumps'],
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
    [],
    exclude_binaries=True,
    name='Pomodoro',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=True,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Pomodoro',
)

app = BUNDLE(
    coll,
    name='Pomodoro.app',
    icon=None,
    bundle_identifier='com.pomodoro.timer',
    info_plist={
        'LSUIElement': True,
        'CFBundleName': 'Pomodoro',
        'CFBundleDisplayName': 'Pomodoro',
        'CFBundleGetInfoString': "Pomodoro Timer",
        'CFBundleIdentifier': "com.pomodoro.timer",
        'CFBundleVersion': "1.0.0",
        'CFBundleShortVersionString': "1.0.0",
        'NSHighResolutionCapable': True,
    }
) 