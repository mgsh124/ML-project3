from gtts import gTTS

AUDIO_PATH = 'static/'


def get_tts(text, image_name):
    audio_url = 'audios/' + image_name[7:-4] + '.mp3'
    tts = gTTS(text)
    tts.save(AUDIO_PATH + audio_url)
    return audio_url