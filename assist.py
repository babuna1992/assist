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
    
def wish():
    hour = int(datetime.datetime.now().hour)
   
    if hour >= 0 and hour<12:
        speak("Hello sir, good morning")
        
    elif hour >= 12 and hour<18:
        speak("Hello sir, good afternoon")
    else:
        speak("Hello sir, good evening")
    
    speak("how can i help you...")

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

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('parameswarbehura07@gmail.com','kfgshkgwoyrexjbs')
    server.sendmail('parameswarbehura07@gmail.com',to,content)
    server.close()
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
        
    
  


        
if __name__ == "__main__":
    wish()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("seraching wikipidia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open facebook" in query:
            webbrowser.open("facebook.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stack overflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "play music" in query:
            music_dir = 'E:\\babul supriyo sarthak'
            songs = os.listdir(music_dir)
            print(songs)
            to = len(songs)
            rand = random.randint(0,to)
            os.startfile(os.path.join(music_dir,songs[rand]))
        elif "the time" in query:
            assistt.wishme()
        elif "hi" in query:
            speak("jai sai ram sir... , how are you..")
        elif "hello" in query:
            speak("jai sai ram sir..., how are you..")
        elif "namaskar" in query:
            speak("jai sri ram..., how are you..")
        elif "madarchod" in query:
            speak("yes sir, sambit is the only good guy in your room.. means you understand what am trying to say...")
        elif "parmeshwar" in query:
            speak("yes parameswar....")
        elif "bore" in query:
            speak("yes sir.. who don't have work they are getting bore like you..")
        elif "pratima" in query:
            speak("Pratima is the only beautyful girl in the world and who is your girl friend")
        elif "sex" in query:
            speak("am not a gay like you.. get out from here.")
        elif "pinky" in query:
            speak("pinky is a beautiful girl and your friend who is living near BTM")
        elif "kalyan" in query:
            speak("kalyani is an angry girl and sister of parameswar")
        elif "boy" in query:
            speak("dhana is strong boy and babuna is weak boy")
        elif "strong" in query:
            speak('dhana is strong boy and babuna is weak boy')
        elif "goodnight" in query:
            speak('very good night sir and madam am also going to sleep')
        elif "how are you" in query:
            speak('i am fine what about you pramod?')
        elif "beauty" in query:
            speak("erectlie boob girl living by side of your room.. and tu setithi kain gaandi maaruchu")
        elif "mantu" in query:
            speak("Mantu is a very sexy boy.... and ghoda gehin also")
        elif 'email to param' in query:
            try:

                speak("what should i write sir?")
                content = takecommand()
                to = "parames.behura@gmail.com"
                sendEmail(to,content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("soory sir am unable to send this mail")
        elif 'email to pramod' in query:
            try:

                speak("what should i write sir?")
                content = takecommand()
                to = "pramodbarik657@gmail.com"
                sendEmail(to,content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("soory sir am unable to send this mail")

        elif "want to send message" in query:
            wpmsg()
            
            
            
