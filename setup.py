import sys
from cx_Freeze import setup, Executable
setup( name = "QrStorm", version = "2.8.3",
       description = "Application which can create QR Codes for Free",
       executables = [Executable("QR Maker_GUI.py",
                                 base = "Win32GUI",
                                 icon="qr-code.ico")])
