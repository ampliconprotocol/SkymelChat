# -*- mode: python -*-

a = Analysis(['skymelchat/__main__.py'],
    pathex=[''],
    binaries=[],
    datas=[
        ( 'skymelchat/graphics/*', 'graphics' ),
        ( 'skymelchat/locale/*', 'locale' ),
        ( 'ffmpeg-*/bin/ffmpeg.exe', '.'),
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[] )

pyz = PYZ(a.pure)

exe = EXE(pyz,
    a.scripts,
    exclude_binaries=True,
    name='SkymelChat.exe',
    strip=False,
    upx=True,
    console=False,
    debug=False,
    icon='skymelchat/graphics/icons/256x256/com.skymel.ico' )

exe_cmd = EXE(pyz,
    a.scripts,
    exclude_binaries=True,
    name='SkymelChat_cli.exe',
    strip=False,
    upx=True,
    console=True,
    debug=True,
    icon='skymelchat/graphics/icons/256x256/com.skymel.ico' )

coll = COLLECT( exe, exe_cmd,
                a.binaries,
                a.zipfiles,
                a.datas,
                strip=False,
                upx=True,
                name='SkymelChat')
