import pyqrcode
import png
from pyqrcode import QRCode

s = input("Enter the url to convert : ")
 
url = pyqrcode.create(s)
 
url.png('myqr.png', scale = 8) 
