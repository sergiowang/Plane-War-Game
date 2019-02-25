# -*- mode: python -*-

block_cipher = None

added_files = [
         ( 'material/image', 'image'),                                     
         ( 'material/sound', 'sound')  # Loads all the .mp3 files from 'folder'.
         ]

a = Analysis(['launcher.py', 'bin\\__init__.py', 'bin\\main.py', 'config\\__init__.py', 'config\\settings.py', 'scr\\__init__.py', 'scr\\bullet.py', 'scr\\enemy.py', 'scr\\myplane.py'],
             pathex=['G:\\PW'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='launcher',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='launcher')
