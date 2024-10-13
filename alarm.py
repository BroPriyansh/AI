import pyttsx3
import datetime
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
extractedtime = open("Alarmtext.txt","rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("Alarmtext.txt","r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("shadow","")
    timenow = timenow.replace("set an alarm","")
    timenow = timenow.replace(" and ",":")
    timenow = timenow.replace("set alarm","")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            speak("Alarm Ringing Sir")
            os.startfile("Demons.mp3")
        elif currenttime + "00:00:30" == Alarmtime:
            exit()
            
ring(time)
