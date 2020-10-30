import qrcode

img = qrcode.make('Aprendendo Python')
img.save('qrcode.png')