import new_vision_audio as nv_aud
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib

def initWish():
    hr = int(datetime.datetime.now().hour)
    if hr >= 0 and hr <12:
        nv_aud.nv_speak("Good morning!")
    elif hr == 12:
        nv_aud.nv_speak("Good Noon!")
    elif hr>12 and hr <18:
        nv_aud.nv_speak("Good Afternoon!")
    else:
        nv_aud.nv_speak("Good Evening!")
    default_str = "Hiii ! I am NewVision, How may I help you today?"
    nv_aud.nv_speak(default_str)

def sendEmail(to, msg):
    srvr = smtplib.SMTP('smtp.gmail.com', 587)
    srvr.ehlo()
    srvr.starttls()
    srvr.login('email', 'password')
    srvr.sendmail('email', to, msg)
    srvr.close()

def hndlWiki(req):
    nv_aud.nv_speak('Hang on ...')
    req = req.replace("wikipedia", "")
    res = wikipedia.summary(req, sentences= 1)
    nv_aud.nv_speak("According to wikipedia...\n")
    print(res)
    nv_aud.nv_speak(res)

def hndlYT():
    webbrowser.open("youtube.com")

def hndlMusic():
        music_dir = "E:\\my_song\\fev"
        song = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, song[random.randint(1,20)]))

def hndlTime():
    curTime = datetime.datetime.now().strftime("%H:%M:%S")
    print("The time is {}".format(curTime))
    nv_aud.nv_speak("Hay! The time is {}".format(curTime))

def hndlVsCode():
    vs_path = "C:\\Users\\Sumagna Dey\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(vs_path)

def hndlMail():
    try:
        print("What do you want to say....  ")
        nv_aud.nv_speak("What do you want to say :- ")
        msg = nv_aud.input_cmd()
        print("Your msg is :-  {}".format(msg))
        to = "deysumagna7@gmail.com"
        sendEmail(to, msg)
        print("Email has been sent! ")
    except Exception as e:
        nv_aud.nv_speak("Sending Failed...")

def goodBye():
    print("Good Bye......")
    nv_aud.nv_speak("Good Bye")