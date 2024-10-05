from yt_dlp import YoutubeDL 
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/getStreamLink/<url>')
def get_info(url):
    # Get format of the video
    ydl = YoutubeDL()
    info = ydl.extract_info(url, download=False)
    url = info['formats'][-1]['url']
    response = jsonify({'url': url})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
