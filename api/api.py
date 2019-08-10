from flask import Flask

app = Flask(__name__)

API_URL = '/project3/api/v1.0'


@app.route(API_URL + '/detect', methods=['GET'])
def detect():
    return 'Hello World through API!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
