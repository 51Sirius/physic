# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\Danil\\Desktop\\проекты\\physic'],
             binaries=[],
             datas=[('20011.ttf', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          name='Physic',
          icon = r"ic.ico",
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False)
