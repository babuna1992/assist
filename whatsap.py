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
import sys
import assistt
import random
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',150)
# print(voices[0].id)
# def speak(audio):
    
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognising...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("say that again please...")
        return "None"
    return query

def wpmsg():
    
    import selenium,time

    from selenium import webdriver

    driver = webdriver.Chrome(r'F:\kilvish\chromedriver.exe')

    driver.maximize_window()

    driver.get('https://web.whatsapp.com/')
    speak('tell me whom you have to message.')
    b = takecommand()
    if b == None:
        speak("tell me again")
    else:
        pass
    name = b.lower()
    print('user said',b)
    speak('enter your message')
    a = takecommand()
    print('user said',a)
    msg = a

   
    speak('can you please press any key.. i want to confirm is that you and please scan your QR code after security confirmation')
    
    input('enter anything after scanning qr code')


    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))

    user.click()

    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

    
    msg_box.send_keys(msg)
    button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
    button.click()
    speak('message has been sent sir')
        
    
wpmsg()   

