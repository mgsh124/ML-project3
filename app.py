from flask import Flask, render_template, redirect, url_for, request
from werkzeug.utils import secure_filename
import requests
import json
import os

API_URL = 'http://web-api:5000/project3/api/v1.0'
UPLOAD_FOLDER = 'static/images/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print('filename', filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('detect', name=filename))
    return render_template('result.html', info={})


@app.route('/detect', methods=['GET', 'POST'])
def detect():
    name = ''
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print('filename', filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('detect', name=filename))
    else:
        name = 'images/' + request.args['name']

    print('name ', name)
    image_result = requests.get(API_URL + '/detect', params={'image_name': name})
    # print(image_result.content)
    print(image_result.json())
    # print(json.loads(image_result.content))
    # info = unicodedata.normalize('NFKD', info.text).encode('ascii','ignore')
    image_result = json.loads(image_result.content) if image_result.content and image_result.json() else {}
    # print(info)

    return render_template('result.html', image_result=image_result, original_image=name)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
