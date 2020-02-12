# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main_exec.py',
              'F:\\useful_tools\\translate\\__init__.py',
              'F:\\useful_tools\\translate\\GetText.py',
              'F:\\useful_tools\\translate\\GoogleTranlator.py',
              'F:\\useful_tools\\translate\\main.py',
              'F:\\useful_tools\\translate\\ph_divide.py',
              'F:\\useful_tools\\translate\\Translator_GUI_v2.py'],
             pathex=['F:\\useful_tools\\translate'],
             binaries=[],
             datas=[],
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
          [],
          exclude_binaries=True,
          name='main_exec',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main_exec')
