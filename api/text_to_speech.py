


from gtts import gTTS
from translate import Translator


AUDIO_PATH = 'static/'


def get_tts(text, image_name):
    audio_url = 'audios/' + image_name[7:-4] + '.mp3'
    tts = gTTS(text)
    tts.save(AUDIO_PATH + audio_url)
    return audio_url

def get_tts_translate(text, image_name,language = 'en'):
    audio_url = 'audios/' + image_name[7:-4] + '_' + language + '_.mp3'

    translator = Translator(to_lang=language)
    translation_text = translator.translate(text)
    #tts = gTTS(text,lang=language, slow=False)
    tts = gTTS(translation_text, lang=language, slow=False)

    tts.save(AUDIO_PATH + audio_url)
    return audio_url,translation_text