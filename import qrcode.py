import qrcode
data="hello"
img=qrcode.make(data==data)
img.save("qr.png")
