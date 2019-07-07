# -*- mode: python -*-

block_cipher = None
import os

spec_root = os.path.abspath(SPECPATH)

a = Analysis([os.path.join(SPECPATH,'SourceFiles','main.py')],
             pathex=[spec_root],
             binaries=[],
             datas=[(os.path.join(SPECPATH,'wolframclient'),'wolframclient'),(os.path.join(SPECPATH,"SourceFiles","definitions.mx"),"."),(os.path.join(SPECPATH,"SourceFiles","repo.mx"),".")],
             hiddenimports=[],
             excludes=["Tkinter","tkinter","tk","tc","_tkinter"],
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
          name='PyMathProblemGenerator',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=True , icon=os.path.join(SPECPATH,"icons","Icon.ico"))
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='PyMathProblemGenerator')
