import speech_recognition as sr
from pocketsphinx import pocketsphinx, Jsgf, FsgModel
# audio_file = '/Users/kapilgupta/Downloads/audio/videoplayback_copy_1.wav'
# text_filename = "/Users/kapilgupta/Downloads/kabcdef"
language_model = '/Users/kapilgupta/opt/anaconda3/lib/python3.9/site-packages/speech_recognition/pocketsphinx-data/en-US/language-model.lm.bin'
acoustic_model = '/Users/kapilgupta/opt/anaconda3/lib/python3.9/site-packages/speech_recognition/pocketsphinx-data/en-US/acoustic-model'
pronunciation_dict = '/Users/kapilgupta/opt/anaconda3/lib/python3.9/site-packages/speech_recognition/pocketsphinx-data/en-US/pronounciation-dictionary.dict'

framerate = 10
config = pocketsphinx.Config()
config.set_string('-hmm', acoustic_model)
config.set_string('-lm', language_model)
config.set_string('-dict', pronunciation_dict)
decoder = pocketsphinx.Decoder(config)

def recognize_sphinx(audio, show_all=True):
    decoder.start_utt()
    decoder.process_raw(audio.get_raw_data(), False, True)
    decoder.end_utt()
    hypothesis = decoder.hyp()
    return decoder, hypothesis.hypstr

# Create a Recognizer instance
r = sr.Recognizer()

# Set the recognize_sphinx() function as the speech recognition method
r.recognize_sphinx = recognize_sphinx

with sr.AudioFile(audio_file) as source:
    audio = r.record(source)
    sample_rate = audio.sample_rate
    decoder, recognized_text = r.recognize_sphinx(audio, show_all=True)


with open(text_filename, 'w') as text_file:
    for seg in decoder.seg():
        segment_info = (seg.word, seg.start_frame/sample_rate, seg.end_frame/sample_rate)
        text_file.write(str(segment_info) + "\n")
print("Text File Successfully Saved")


