# -*- mode: python -*-

block_cipher = None


a = Analysis(['/Users/zero/Desktop/F4T Dictionary/rdict/src/main/python/main.py'],
             pathex=['/Users/zero/Desktop/F4T Dictionary/rdict/target/PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['/usr/local/lib/python3.7/site-packages/fbs/freeze/hooks'],
             runtime_hooks=['/var/folders/y4/tksrb0ln6bqd12r35dlg8c1c0000gq/T/tmp5w2asn2q/fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='F4T Dictionary',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , icon='/Users/zero/Desktop/F4T Dictionary/rdict/target/Icon.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='F4T Dictionary')
app = BUNDLE(coll,
             name='F4T Dictionary.app',
             icon='/Users/zero/Desktop/F4T Dictionary/rdict/target/Icon.icns',
             bundle_identifier=None)
