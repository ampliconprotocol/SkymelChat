# -*- mode: python -*-

a = Analysis(['skymelchat/__main__.py'],
    pathex=[''],
    binaries=[
        ('ffmpeg', '.'),
    ],
    datas=[
        ( 'skymelchat/graphics/*', 'graphics' ),
        ( 'skymelchat/locale/*', 'locale' ),

    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[] )

pyz = PYZ(a.pure)

exe = EXE(pyz,
    a.scripts,
    exclude_binaries=True,
    name='SkymelChat',
    strip=False,
    upx=True,
    console=False,
    debug=False,
)

coll = COLLECT( exe,
                a.binaries,
                a.zipfiles,
                a.datas,
                strip=False,
                upx=True,
                name='SkymelChat')

app = BUNDLE(coll,
    name='SkymelChat.app',
    icon='skymelchat/graphics/icons/512x512/com.skymel.icns',
    bundle_identifier='com.skymelchat',
    info_plist={
            'CFBundleShortVersionString': '21.09.01.01',
            'CFBundleVersion':'21.09.01.01'
    })
