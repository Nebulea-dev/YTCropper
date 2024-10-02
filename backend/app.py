from yt_dlp import YoutubeDL 
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/<url>')
def get_info(url):
    ydl = YoutubeDL()
    info = ydl.extract_info(url, download=False)
    return info
