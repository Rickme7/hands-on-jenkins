from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://media3.giphy.com/media/VeHBSH9F4GZpuuic00/giphy.webp",
    "https://media1.giphy.com/media/iDJQRjTCenF7A4BRyU/giphy.webp",
    "https://media1.giphy.com/media/ZNegC7wFpuQT7nurZ0/200w.webp",
    "https://media4.giphy.com/media/YHSaTzT2Hg11xKuYMM/giphy.webp",
    "https://media1.giphy.com/media/eYilisUwipOEM/200.webp",
    "https://media1.giphy.com/media/21PV0Su6USswD76iLv/200w.webp",
    "https://media2.giphy.com/media/JTaHahqEVizjwKuc7e/200w.webp",
    "https://media2.giphy.com/media/xT0xeuOy2Fcl9vDGiA/200w.webp",
    "https://media4.giphy.com/media/VFDeGtRSHswfe/200w.webp",
    "https://media3.giphy.com/media/3ohzdYGKrPn8GzgAes/200w.webp",
    "https://media1.giphy.com/media/9DctaOQnk7GX0LIxj9/giphy.webp",
    "https://media1.giphy.com/media/2RQTroUuvLTYGySHJa/giphy.webp",
    "https://media2.giphy.com/media/KEh5kliRTSVJm/200w.webp",
    "https://media3.giphy.com/media/fJdpdS5jaDje8/200w.webp",
    "https://media1.giphy.com/media/iIXTaiiEf0jy4gHFFZ/giphy.webp"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
