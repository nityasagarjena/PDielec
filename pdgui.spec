# -*- mode: python -*-

block_cipher = None


a = Analysis(['pdgui.py'],
             pathex=['C:\\Users\\pdielec\\Software\\PDielec'],
             binaries=[],
             datas=[('c:\\Users\\pdielec\\Software\\PDielec\\Examples','Examples')],
             hiddenimports=['scipy._lib.messagestream'],
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
          name='pdgui',
          debug=False,
          strip=False,
          upx=True,
          console=False,
	  icon='C:\\Users\\pdielec\\Software\\PDielec\\Sphinx\\_static\\Figures\\infrared.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='pdgui')
