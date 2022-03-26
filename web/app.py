import json
import requests
from flask import Flask, render_template, request
import os
from gtts import gTTS
from playsound import playsound

if os.environ.get('DOCKER', 'False') == 'True':
    UPLOAD_FOLDER = '/usr/src/app/images'
else:
    UPLOAD_FOLDER = 'images'

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/uploader', methods=['POST'])
def upload_file():
    NO_VALID_IMAGE = 'No se ha proporcionado ninguna imagen válida'

    if request.method == 'POST' and request.files:
        f = request.files['image']

        try:
            response = requests.post('http://nginx:80/upload', files={'upload_file': f})
            respuesta_api = json.loads(response.content)
        except Exception as e:
            return render_template('results.html', text=NO_VALID_IMAGE)

        if not os.environ.get('DOCKER', 'False'):
            myobj = gTTS(text=respuesta_api, lang='es', slow=False)
            myobj.save(app.config['UPLOAD_FOLDER'] + '/speech.mp3')
            playsound(app.config['UPLOAD_FOLDER'] + '/speech.mp3')

        return render_template('results.html', text=respuesta_api['texto']) 

    else:
        return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)