from flask import Flask, request
import tensorflow as tf

app = Flask(__name__)

API_URL = '/project3/api/v1.0'

from .object_detection import detect_object, init_model


model = init_model()
graph = tf.get_default_graph()


@app.route(API_URL + '/detect', methods=['GET'])
def detect():
    global graph
    with graph.as_default():
        image_name = request.args.get('image_name')
        detected_image = detect_object(model, image_name)
        return {'img_url': detected_image}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
