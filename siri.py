import speech_recognition as sr
from termcolor import colored
from datetime import datetime
import webbrowser
from time import sleep
from gtts import gTTS
from playsound import playsound
import random
import os

r = sr.Recognizer()


def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.record(source, duration=4)
        voice = ''
        try:
            voice = r.recognize_google(audio, language='tr-TR')
        except sr.UnknownValueError:
            speak("Anlayamadım.")
        except sr.RequestError:
            speak("Sistem çalışmıyor.")
        return voice


def response(voice):
    if 'nasılsın' in voice:
        speak('iyiyim sen nasılsın?')
    if 'saat kaç' in voice:
        speak(datetime.now().strftime('%H:%M:%S'))
    if 'arama yap' in voice:
        search = record('ne aramak istiyorsun')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak(search + ' için internette bulduklarım ')
    if 'tamamdır' in voice:
        speak('görüşürüz')
        exit()


def speak(string):
    tts = gTTS(string, lang='tr')
    rand = random.randint(1, 10000)
    file = 'audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)


speak('sana nasıl yardımcı olabilirim')
sleep(1)

while 1:
    voice = record()
    print(colored(voice, "blue"))
    response(voice)
