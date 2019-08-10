from flask import Flask, render_template, redirect, url_for, request
import requests

app = Flask(__name__)

API_URL = 'http://localhost:5000/project3/api/v1.0'


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/detect')
def detect():
    # print(json.loads(request.args['message']))
    # data = json.loads(request.args['message'])
    info = requests.get(API_URL + '/detect', params={})
    print(info.content)
    # info = unicodedata.normalize('NFKD', info.text).encode('ascii','ignore')
    # info = json.loads(info)
    print(info)
    return render_template('result.html', info=info)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
