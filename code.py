import pyqrcode
import png
from pyqrcode import QRCode

QRstring = "....." #Copy any url code you want
url = pyqrcode.create(QRstring)
url.png('Desktop\\qr.png', scale = 8)
