# from django.test import TestCase

# Create your tests here.
import pyqrcode

from pyqrcode import QRCode
  
  
# String which represents the QR code
s = "aaris4"
  
# Generate QR code
url = pyqrcode.create(s)
print(url)
  
# Create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale = 8)
print(url.svg("myqr.svg",scale = 8))
  
# Create and save the png file naming "myqr.png"
# url.png('myqr.png', scale = 6)