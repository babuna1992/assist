import pyaudio
import pyttsx3
import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',150)
# print(voices[0].id)
# def speak(audio):
    
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    minute = int(datetime.datetime.now().minute)
    if hour >= 0 and hour<12:
        speak("sir, the time now is"+str(hour)+"and"+str(minute)+"in the morning")
        
    elif hour >= 12 and hour<18:
        speak("sir, the time now is"+str(hour)+"and"+str(minute)+"in the after noon")
    else:
        speak("the time now is"+str(hour)+"and"+str(minute)+"in the evening")
    
    speak("hello am Jarvish, how can i help you sir?")
