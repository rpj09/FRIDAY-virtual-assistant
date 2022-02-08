from __future__ import unicode_literals
import requests
from functools import cache,lru_cache
import speech_recognition as sr
import datetime
import os
from requests import get
import webbrowser
import pywhatkit as kit
import wikipedia
import pyautogui
from tkinter import *
from tkinter.ttk import *
from time import sleep, strftime
import time
from gtts import gTTS
from playsound import playsound
import sys
import smtplib
import threading
import pyjokes



#text to speech


fridi=('')
def speak(audio):
    kk  = gTTS(text=audio, lang='en-us', slow=False)
    kk.save("aua.wav")
    global fridi
    fridi=audio
    print(audio)
    playsound("aua.wav")





def takequery():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.adjust_for_ambient_noise(source)
        #r.energy_threshold = 1932
        #r.dynamic_energy_threshold = True

        print("Say something!")
        audio = r.listen(source,timeout=2,phrase_time_limit=3.5 )
        #audio = r.record(source, duration = 4)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio,language='en-in')
        print(f'user said : {query}')
    except Exception as e:
        speak('say that again please...')
        return 'none'
    query = query.lower()
    return query





def wakeup():

    r = sr.Recognizer()
    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source)

        audio = r.listen(source,timeout=2,phrase_time_limit=3.5 )

    try:
        query = r.recognize_google(audio,language='en-in')
    except Exception as e:
        return 'none'
    query = query.lower()
    return query



#to wish

def wish():
    hour = (datetime.datetime.now().hour)
    e = datetime.datetime.now()
    ex=("%s:%s" % (e.hour, e.minute))


    if hour>=0 and hour<=12:
        speak(f"good morning sir, its {ex} AM")
    elif hour>12 and hour<18:
        ex=("%s:%s" % (e.hour-12, e.minute))
        speak(f"good afternoon sir, its {ex} PM")
    else:
        ex=("%s:%s" % (e.hour-12, e.minute))
        speak(f"good evening sir, its {ex} PM")
    speak("I'm FRIDAY ,please tell me how can i help you")




# to continously update fridi value
def aut():
    return fridi





def gui():
    
    global root
    root = Tk()
    root.title("F . R . I . D . A . Y")

    def time():
        string = strftime('%H:%M:%S %p')
        fridi=aut()
        label.config(text=fridi)
        label.after(10000,time)
        label1.config(text=string)
        label1.after(1000,time)


    label=Label(root, font=("ds-digital",35), background= 'black', foreground='cyan')
    label1=Label(root, font=("ds-digital",25), background= 'black', foreground='cyan')

    label1.pack(anchor='center')
    label.pack(anchor='s',side='bottom')

    root.configure(bg='black')
    time()

    root.mainloop()





def online_class():
    try:
        import pickle
        speak("which class do you want to join sir?")
        classes=takequery()
        speak(f"joining {classes} class")
        file=open("online_class_links.dat","rb")
        data = pickle.load(file)
        g_links = data[classes]
        webbrowser.open(g_links)
        pyautogui.sleep(10)
        pyautogui.keyDown('winleft')
        pyautogui.press('up')
        pyautogui.keyUp('winleft')
        pyautogui.sleep(1)
        pyautogui.keyDown('ctrl')
        pyautogui.press('d')
        pyautogui.sleep(1)
        pyautogui.keyDown('ctrl')
        pyautogui.press('e')
        pyautogui.keyUp('ctrl')

        #press_and_release('ctrl + d')
        #press_and_release('ctrl + e')
        #pyautogui.click(x=427, y=614) #mic
        #pyautogui.click(x=486, y=626) #camera
        pyautogui.sleep(1)
        pyautogui.click(x=988, y=484)#ask to join
        file.close()
    except:
        speak('there was a error while joining the class.')




def ytvideodownload():
    try:
        from pytube import YouTube
        from pyautogui import click
        from pyautogui import hotkey
        #import pyperclip
        from time import sleep
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        #press_and_release('win + up')
        sleep(2)
        click(x=580, y=86)
        hotkey('ctrl','a')
        hotkey('ctrl','c')
        value = root.clipboard_get()#pyperclip.paste()
        Link = str(value) # Important
    except Exception as e:
        speak('Sorry sir ! There was a error while downloading the video')

    def Download(link):
        url = YouTube(link)
        video = url.streams.first()
        video.download('\Home\F.R.I.D.A.Y\ytdownloads')
        '''
        import youtube_dl

        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        '''
    speak('Downloading this video')
    Download(Link)
    speak("Done Sir , I Have Downloaded The Video .")
    speak("You Can Go And Check It Out.")




def sendEmail(to,content):
    import pickle
    with open("mail.pickle","rb") as file:
        data = pickle.load(file)
        email = data['email']
        password=data['password']
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(f'{email}',f'{password}')
    server.sendmail(email, to, content)
    server.close()



def my_loaction():
    ip_add= requests.get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/'+ip_add+'.json'
    geo_q=requests.get(url)
    geo_d=geo_q.json()
    state=geo_d['city']
    country = geo_d['country']
    speak(f'Sir,You are Now in {state},',f'{country}.')



def whatsapp():
    try:
        import pickle  # importing module
        speak('Whom do want to send message')
        c = takequery()
        with open("first_pickle.pickle","rb") as file:
            data = pickle.load(file)
            num = data[c]
        speak('what message do you want to send')
        cm = takequery()
        kit.sendwhatmsg(f'+91{num}',f'{cm}',datetime.datetime.now().hour,datetime.datetime.now().minute+1)
        speak("message sent!")
    except Exception as e:
        speak('there was a error while sending the message')



def automations():
    start = time.time()
    wish()
    while True:

        try:
            query = takequery()
            print(time.time()-start)


            #logic building for task
            if 'hello' in query:
                speak("hello. it's good to hear from you.")
                speak("I hope you and your loved ones are staying safe and healthy during this difficult time.")
            
            elif 'do you know Alexa' in query:
                speak('yeah! it is a AI made by amazon ')
            elif 'Is alexa better than you' in query:
                speak('yepp! but i know You will make me one of his competitor soon ')
            elif 'location' in query:
                my_loaction()
            elif 'open whatsapp' in query:
                webbrowser.open('https://web.whatsapp.com/')

            elif 'open youtube' in query:
                webbrowser.open('https://www.youtube.com/')
            elif 'joke' in query or 'comedy' in query:
                jk = pyjokes.get_joke(language="en", category="all")
                speak(jk)
                print(jk)
            elif 'joke' in query:
                speak(pyjokes.get_joke())
        
        
        
            elif 'open chrome' in query:
                speak("Okay sir, opening chrome") 
                os.system('google-chrome')
            if 'chrome new tab' in query:
                pyautogui.keyDown('ctrl')
                pyautogui.press('t')
                pyautogui.sleep(1)
                pyautogui.keyUp('ctrl')
                speak('done sir')
            elif 'chrome close tab' in query:
                pyautogui.keyDown('ctrl')
                pyautogui.press('w')
                pyautogui.sleep(1)
                pyautogui.keyUp('ctrl')
                speak('closed')
            elif 'chrome new window' in query:
                pyautogui.keyDown('ctrl')
                pyautogui.press('n')
                pyautogui.sleep(1)
                pyautogui.keyUp('ctrl')
                speak('here it is')
            elif 'chrome history' in query:
                pyautogui.keyDown('ctrl')
                pyautogui.press('h')
                pyautogui.sleep(1)
                pyautogui.keyUp('ctrl')
                speak('here it is')
            elif 'chrome show downloads' in query:
                pyautogui.keyDown('ctrl')
                pyautogui.press('j')
                pyautogui.sleep(1)
                pyautogui.keyUp('ctrl')
                speak('here it is')
            elif 'chrome bookmark this tab' in query:
                pyautogui.keyDown('ctrl')
                pyautogui.press('d')
                pyautogui.sleep(1)
                pyautogui.keyUp('ctrl')
                pyautogui.press('enter')
                speak('done')
            elif 'chrome incognito' in query:
                pyautogui.keyDown('ctrl')
                pyautogui.keyDown('shift')
                pyautogui.press('n')
                pyautogui.sleep(1)
                pyautogui.keyUp('ctrl')
                pyautogui.keyUp('shift')
                speak('here it is')
            elif 'chrome switch tab' in query:
                tab = query.replace("switch tab ", "")
                Tab = tab.replace("to","") 
                TaB = Tab.replace('chrome','')      
                num = TaB
                pyautogui.keyDown('ctrl')
                pyautogui.press(f'{num}')
                pyautogui.sleep(1)
                pyautogui.keyUp('ctrl')
            
            elif "download this video" in query:
                ytvideodownload()
            
            elif 'close this' in query:
                pyautogui.keyDown('alt')
                pyautogui.press('f4')
                pyautogui.sleep(1)
                pyautogui.keyUp('alt')

            elif 'minimise all' in query:
                speak('minimising all')
                pyautogui.keyDown('winleft')
                pyautogui.press('d')
                pyautogui.sleep(1)
                pyautogui.keyUp('winleft')  
                        

            elif 'according to wikipedia' in query:
                speak("searching wikipedia")
                query = query.replace('according to wikipedia','')
                results = wikipedia.summary(query,sentences=2)
                speak('according to wikipedia')
                speak(results)
                print(results)
            
            
            elif 'play' in query:
                query=query.replace('play','')
                pyautogui.press('winleft')
                pyautogui.click(x=766, y=84)
                pyautogui.write(query)
                pyautogui.press('enter')

            
            elif 'system open' in query:
                query=query.replace('system open','')
                pyautogui.press('winleft')
                pyautogui.click(x=766, y=84)
                pyautogui.write(query)
                pyautogui.press('enter')
            
            
            
            
            elif 'open zoom' in query: 
                os.system('Zoom')
            elif "open settings" in query:
                os.system("gnome-control-center")     
            elif 'ip address' in query:
                ip = get('https://api.ipify.org').text
                speak(f'your ip address is {ip}')
            elif "switch the window" in query or "switch window" in query:
                speak("Okay sir, Switching the window")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)   
                pyautogui.keyUp("alt")

            elif "class" in query:
                online_class()

            elif 'open youtube' in query:
                webbrowser.open('https://www.youtube.com')
            
            elif 'open youtube music' in query:
                webbrowser.open('https://music.youtube.com')
            
            elif 'google' in query:
                speak('sir,what should i search on google')
                cm =takequery()
                webbrowser.open(f'{cm}')

            elif 'search' in query:
                query=query.replace('search','')
                webbrowser.open(query)

            elif 'contacts' in query:
                speak("ye liiijiiiyee sir!")
                import pickle  # importing module
                with open("first_pickle.pickle","rb") as file:
                    data = pickle.load(file)
                    print(data)
                        
                

            elif 'mail' in query:
                import pickle
                speak('whom do you want to send mail')
                to=takequery()
                with open("mail.pickle","rb") as file:
                    data = pickle.load(file)
                    to = data[f"{to}"]
                


                speak('what do you want to send sir')
                content=takequery()    
                sendEmail(to,content) 
                speak('mail sent')

            elif 'message' in query:
                whatsapp()

            elif 'play a video on youtube' in query:
                speak("what kind of video do you want to play! sir?")
                cm = takequery()
                kit.playonyt(f"{cm}")
            
            elif 'hibernate' in query:
                speak('bye sir! hope you enjoyed the day')
                os.system(("shutdown /h"))
            elif 'shutdown' in query:
                speak('bye sir! hope you enjoyed the day')
                os.system(("shutdown /s"))
            elif 'restart' in query:
                speak('bye sir! hope you enjoyed the day')
                os.system(("shutdown /r"))
            elif 'nikal' in query:
                speak('मैं नहीं जाऊंगी, तुम जाओ बेवकूफ, तुम यह भी नहीं जानते कि कैसे बात करनी है')
            elif 'zindagi' in query or 'jindagi' in query:
                speak('शानदार  मज़ेदार')
            elif 'exit' in query or 'go offline' in query or 'rest' in query:
                speak('Sure sir! have a nice day')
                break
        
        except Exception as e:
            print(e)
            speak(e)
        


if __name__ == '__main__': 
    while True:
        permission = wakeup()
        print(permission)
        try:
            if "friday" in permission or 'alpha' in permission:
                t1=threading.Thread(target=gui)
                t1.start()
                automations()
                
            elif "break" in permission:
                speak('going offline') 
                sys.exit()
        except Exception as e:
            print(e)     
        
       
        


        
        



