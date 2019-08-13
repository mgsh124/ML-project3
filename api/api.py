from flask import Flask, request
import tensorflow as tf
import os

from .object_detection import detect_object, init_model
from .image_captioning import get_caption_model, get_encode_img_model, predict_captions
from .text_to_speech import get_tts

app = Flask(__name__)

API_URL = '/project3/api/v1.0'
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

object_detection_model = init_model()
image_caption_model = get_caption_model()
encode_img_model = get_encode_img_model()
graph = tf.get_default_graph()


@app.route(API_URL + '/detect', methods=['GET'])
def detect():
    global graph
    with graph.as_default():
        image_name = request.args.get('image_name')
        detected_image = detect_object(object_detection_model, image_name)
        captions = predict_captions(encode_img_model, image_caption_model, image_name)
        audio = get_tts(captions, image_name)
        return {'img_url': detected_image, 'captions': captions, 'audio_url': audio}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
