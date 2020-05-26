import pyttsx3
import speech_recognition as sr

vc_engine = pyttsx3.init('sapi5')
nv_voice = vc_engine.getProperty('voices')
vc_engine.setProperty('voice', nv_voice[1].id)

def nv_speak(aud):
    vc_engine.say(aud)
    vc_engine.runAndWait()

def input_cmd():
    recog = sr.Recognizer()
    with sr.Microphone() as source:                                                                      
        print("I am listening...")
        audio = recog.record(source,duration=4)
    try:
        req=recog.recognize_google(audio)
        print(req)
    except:
        print("Please check your mic !")
        return "None"
    return req