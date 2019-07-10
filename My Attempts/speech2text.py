#import library
import speech_recognition as sr

# initialize our source
r = sr.Recognizer()

# Mentioning about our source
with sr.Microphone() as source:
    print('speak anything : ')
    audio = r.listen(source)
    # try
    # Recognizer Converting into text
    text = r.recognize_google(audio)
    print('You said : {}'.format(text))
    # except
    print('Sorry Coudnt Recognized yo voice')


#PyAudio error might occur constantly though you install pip install pip audio/ pip install SpeechRocognition
# Download the relavant version of pyaudio from (https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and pip install (downloaded file)