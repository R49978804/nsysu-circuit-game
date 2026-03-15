import qrcode

url = "https://nsysu-circuit-game-ukojsrrq2ahqmzc6ybyprh.streamlit.app/"

img = qrcode.make(url)

img.save("game_qrcode.png")

print("QR Code 已產生")