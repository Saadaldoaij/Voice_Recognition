# You should download speech_recognition and pyaudio librarys
''' <<------- Type in the CMD ---->> 
pip install SpeechRecognition
pip install pipwin
pipwin install pyaudio
# 
# '''
import speech_recognition as sr
import pyaudio
r = sr.Recognizer()

with sr.Microphone() as source:
    print('Say Anything')
    r.adjust_for_ambient_noise(source, duration=0.5)
    a = r.listen(source)

    try:
        text = r.recognize_google(a)
        print(f'You said {text}')
    except:
        r = sr.Recognizer()
