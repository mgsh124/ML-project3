# based on https://github.com/Faizan-E-Mustafa/Image-Captioning
import pickle
import numpy as np
from keras.preprocessing import sequence, image
from keras.models import load_model, Model
from keras.applications.inception_v3 import InceptionV3

DATA_PATH = 'data'
IMAGE_PATH = 'static/'


def preprocess_input(x):
    x /= 255.
    x -= 0.5
    x *= 2.
    return x


def preprocess(image_path):
    img = image.load_img(image_path, target_size=(299, 299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    x = preprocess_input(x)
    return x


def get_caption_model():
    model = load_model(DATA_PATH + '/imageCaption20.h5')
    print("Image captioning model loaded")
    # model.summary()
    return model


def get_encode_img_model():
    model = InceptionV3(weights=DATA_PATH + '/inception_v3_weights_tf_dim_ordering_tf_kernels.h5')
    new_input = model.input
    new_output = model.layers[-2].output

    model_new = Model(new_input, new_output)
    print('Encode image model loaded')
    return model_new


def encode(model, image):
    image = preprocess(image)
    temp_enc = model.predict(image)
    temp_enc = np.reshape(temp_enc, temp_enc.shape[1])
    return temp_enc


def processing():
    vocab = pickle.load(open(DATA_PATH + '/vocab.p', 'rb'))
    print(len(vocab))

    word_idx = {val: index for index, val in enumerate(vocab)}
    idx_word = {index: val for index, val in enumerate(vocab)}

    return word_idx, idx_word


def predict_captions(encode_img_model, image_caption_model, image_name):
    start_word = ["<start>"]
    max_length = 40

    word_idx, idx_word = processing()
    encode_img = encode(encode_img_model, IMAGE_PATH + image_name)

    while 1:
        now_caps = [word_idx[i] for i in start_word]
        now_caps = sequence.pad_sequences([now_caps], maxlen=max_length, padding='post')
        e = encode_img
        preds = image_caption_model.predict([np.array([e]), np.array(now_caps)])
        word_pred = idx_word[np.argmax(preds[0])]
        start_word.append(word_pred)

        if word_pred == "<end>" or len(start_word) > max_length:
            # keep on predicting next word unitil word predicted is <end> or caption lenghts is greater than max_lenght(40)
            break

    return ' '.join(start_word[1:-1])
