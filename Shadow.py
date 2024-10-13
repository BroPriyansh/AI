import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyautogui
import requests
from bs4 import BeautifulSoup
from pynput.keyboard import Key,Controller
from time import sleep


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Eveningk")
        
    speak("I am Shadow , How may I help you")
    
def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

keyboard = Controller()

def volumeup():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)
def volumedown():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)

def takeCommand():
    ''' It yake michrophone input from use
    and returns string output'''
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
        
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query
        

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        
        if 'wake up' in query:
            wishMe()
            while True:
                query = takeCommand().lower()
            
                if 'wikipedia' in query:
                    speak("Searching Wikipedia...")
                    query = query.replace("wikipedia","")
                    results = wikipedia.summary(query, sentences=1)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
            
                # elif 'open youtube' in query:
        
                #     webbrowser.open("youtube.com")
        
                # elif 'open google' in query:
                #     webbrowser.open("google.com")
            
                elif 'open' in query:
                    query = query.replace("open","")
                    query = query.replace("shadow","")
                    query = query.replace("please","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("Enter")
            
                elif 'temperature' in query:
                    search = "Temperature in Agra"
                    url = f"https://www.google.com/search?q={search}" 
                    r = requests.get(url) 
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"Current {search} is {temp}")
            
                elif 'weather' in query:
                    search = "Weather in Agra"
                    url = f"https://www.google.com/search?q={search}" 
                    r = requests.get(url) 
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"Current {search} is {temp}")
            
                elif 'set an alarm' in query:
                    print("Input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time:-")
                    alarm(a)
                    speak("Done,Sir")
            
                elif 'pause' in query:
                    if 'video' in query:
                        pyautogui.press("k")
                        speak("video paused")
                    elif 'music' or 'song' in query:
                        pyautogui.press('space')
                        speak("Pauseing song")
        
                elif 'play' in query:
                    if 'video' in query:
                        pyautogui.press("k")
                        speak("video play")
                    elif 'music' or 'song' in query:
                        pyautogui.press('space')
                        speak("Playing song")
            
                elif 'mute' in query:
                    pyautogui.press("m")
                    speak("video muted")
            
                elif 'volume up' in query:
                    speak("Turning volume up,Sir")
                    volumeup()
            
                elif 'volume down' in query:
                    speak("Turning volume down,Sir")
                    volumedown()
            
                elif 'next' in query:
                    if 'video' in query:
                        pyautogui.press("N")
                        speak("Playing next video")
                    elif 'music' or 'song' in query:
                        pyautogui.hotkey('ctrl','right')
                        speak("Playing next song")
            
                elif 'previous' in query:
                    if 'video' in query:
                        pyautogui.press("P")
                        speak("Playing previous video")
                    elif 'music' or 'song' in query:
                        pyautogui.hotkey('ctrl','left')
                        speak("Playing previous song")

                elif 'search' and 'on youtube' in query:
                    search = query.replace("search","")
                    search = search.replace("on youtube","")
                    webbrowser.open(f"https://www.youtube.com/results?search_query={search}")
                    speak(f"Searching {search} on youtube")
                    
                elif 'search' and 'on google' in query:
                    search = query.replace("search","")
                    search = search.replace("on google","")
                    webbrowser.open(f"https://duckduckgo.com/?t=ffab&q={search}")
                    speak(f"Searching {search} on youtube")
                    
                elif 'stop program' or 'shutdown' in query:
                    speak("Stopping")
                    break;
        
        elif 'shutdown' in query:
            speak("Its been a pleasure working with you, GoodBye")
            break;
        
        else:
            print("Sorry, currently asleep")