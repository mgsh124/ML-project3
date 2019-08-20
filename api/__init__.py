from flask import Flask, request
import tensorflow as tf
import os

API_URL = '/project3/api/v1.0'
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
graph = tf.get_default_graph()


def create_app():
    app = Flask(__name__)

    from .object_detection import detect_object, init_model
    from .image_captioning import get_caption_model, get_encode_img_model, predict_captions
    from .text_to_speech import get_tts,get_tts_translate

    object_detection_model = init_model()
    image_caption_model = get_caption_model()
    encode_img_model = get_encode_img_model()

    @app.route(API_URL + '/detect1', methods=['GET'])
    def detect1():
        return "123"

    @app.route(API_URL + '/detect', methods=['GET'])
    def detect():
        global graph
        with graph.as_default():
            image_name = request.args.get('image_name')
            language = request.args.get('language')

            detected_image = detect_object(object_detection_model, image_name)
            captions = predict_captions(encode_img_model, image_caption_model, image_name)

            #audio = get_tts(captions, image_name)
            audio,translatedCaption = get_tts_translate(captions, image_name,language)

            #return {'img_url': detected_image, 'captions': captions, 'audio_url': audio}
            return {'img_url': detected_image, 'captions': translatedCaption, 'audio_url': audio}

    return app
