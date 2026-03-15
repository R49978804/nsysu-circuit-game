import qrcode

url = "https://github.com/R49978804/nsysu-circuit-game.git"

img = qrcode.make(url)

img.save("game_qrcode.png")

print("QR Code 已產生")