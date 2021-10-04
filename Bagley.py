#     __  __     _ __  __         _ __  
#    / / / /____(_) /_/ /_ _   __(_) /__
#   / /_/ / ___/ / __/ __ \ | / / / //_/
#  / __  / /  / / /_/ / / / |/ / / ,<   
# /_/ /_/_/  /_/\__/_/ /_/|___/_/_/|_|                                      
#   ______          __                __            _          
#  /_  __/__  _____/ /_  ____  ____  / /___  ____ _(_)__  _____
#   / / / _ \/ ___/ __ \/ __ \/ __ \/ / __ \/ __ `/ / _ \/ ___/
#  / / /  __/ /__/ / / / / / / /_/ / / /_/ / /_/ / /  __(__  ) 
# /_/  \___/\___/_/ /_/_/ /_/\____/_/\____/\__, /_/\___/____/  
#                                         /____/

#Libraries needed for the program
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import os
import sys
import subprocess
import random

print("     __  __     _ __  __         _ __   ")
print("    / / / /____(_) /_/ /_ _   __(_) /__ ")
print("   / /_/ / ___/ / __/ __ \ | / / / //_/ ")
print("  / __  / /  / / /_/ / / / |/ / / ,<    ")
print(" /_/ /_/_/  /_/\__/_/ /_/|___/_/_/|_|   ")
print("   ______          __                __            _           ")
print("  /_  __/__  _____/ /_  ____  ____  / /___  ____ _(_)__  _____ ")
print("   / / / _ \/ ___/ __ \/ __ \/ __ \/ / __ \/ __ `/ / _ \/ ___/ ")
print("  / / /  __/ /__/ / / / / / / /_/ / / /_/ / /_/ / /  __(__  )  ")
print(" /_/  \___/\___/_/ /_/_/ /_/\____/_/\____/\__, /_/\___/____/   ")
print("                                         /____/ ")

#What are the things while taking Query from user
def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening...')

        r.pause_threshold = 0.7
        audio = r.listen(source)

        try:
            print("Recognizing...")

            Query = r.recognize_google(audio,language='en-in')
            print("You said=", Query)

        except Exception as e:
            print(e)
            speak("Sorry, I didn't understand. Can you rephrase it??")
            return "None"

        return Query

#Voice Property of the program
def speak(audio):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[0].id)

    print('Bagley:' + audio)
    engine.say(audio)
    engine.runAndWait()

def tellDay():
    day = datetime.datetime.today().weekday() + 1
    
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 
                6: 'Saturday', 
                7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)
        
def tellTime():
    
    time = str(datetime.datetime.now())
    
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is" + hour + "Hours and" + min + "Minutes")
    
#When Activated the program things to start with
def Hello():
    
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')
        
    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')
        
    if currentH >= 18 and currentH != 0:
        speak('Good Evening!')
    
    speak("How can i help you today?")

def Take_query():
    Hello()

    while(True):

        query = takeCommand().lower()

        # Websites opening commands

        if "open youtube" in query:
            speak("Opening Youtube")
            webbrowser.open("www.youtube.com")
            continue

        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("www.google.com")
            continue

        elif "open classroom" in query:
            speak("Opening Google Classroom")
            webbrowser.open("https://classroom.google.com/u/1/h")
            continue

        elif "open google meet" in query:
            speak("Opening Google Meet")
            webbrowser.open("https://meet.google.com")
            continue

        elif "open speedtest" in query:
            speak("Opening speedtest")
            webbrowser.open("https://www.speedtest.net/")
            continue

        elif "open gmail" in query:
            speak("Opening Google Mail")
            webbrowser.open("https://mail.google.cin/mail/u/0/#inbox")
            continue

        elif "open netflix" in query:
            speak("Opening Netflix")
            webbrowser.open("https://netflix.com")
            continue

        elif "open prime video" in query:
            speak("Opening Prime Video")
            webbrowser.open("https://www.primevideo.com")
            continue

        elif "open studio" in query:
            speak("Opening Youtube Studio")
            webbrowser.open("https://studio.youtube.com/channel/UCj-YgHAXSK2R62hMOytdMew?c=UCj-YgHAXSK2R62hMOytdMew")
            continue

        elif "open drive" in query:
            speak("Opening Google Drive ")
            webbrowser.open("https://drive.google.com")
            continue

        elif "open github" in query:
            speak("Opening Github")
            webbrowser.open("https://github.com")
            continue

        #Local application opening commands
# In order to open more applications through the program you need to specify it's path in the code. eg:
           # elif "your command" in query:
           # speak("What to say after listening the user")
           # os.system("application name if downloaded from microsoft store")
           # subprocess.Popen("Path of the application")
           # continue

        elif "open spotify" in query:
            speak("Opening Spotify")
            os.system("Spotify")
            continue

        elif "open virtualbox" in query:
            speak("Opening Virtual Box")
            subprocess.Popen("C:\Program Files\Oracle\VirtualBox\VirtualBox.exe")
            #os. system("Oracle VM VirtualBox")
            continue
        
        elif "open anydesk" in query:
            speak("Opening Anydesk")
            subprocess.Popen("C:\Program Files (x86)\AnyDesk\AnyDesk.exe")
            #os.system('C:\Program Files (x86)\AnyDesk\AnyDesk.exe')
            continue
        
        elif "illustrator" in query:
            speak("Opening Adobe Lightroom")
            subprocess.Popen("C:\Program Files\Adobe\Adobe Illustrator 2021\Support Files\Contents\Windows\Illustrator.exe")
            continue
        
        elif "open photoshop" in query:
            speak("Opeing Adobe Photoshop")
            subprocess.Popen("C:\Program Files\Adobe\Adobe Photoshop CC 2019\Photoshop.exe")
            continue
        
        elif "open premiere pro" in query:
            speak("Opening Adobe Premiere Pro")
            subprocess.Popen("C:\Program Files\Adobe\Adobe Premiere Pro 2021\Adobe Premiere Pro.exe")
            continue
        
        elif "open epic games" in query:
            speak("Opening Epic Games Launcher")
            subprocess.Popen("C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe")
            #os. system("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Epic Games Launcher.lnk")
            continue
        
        elif "open pycharm" in query:
            speak("Opening PYCharm")
            subprocess.Popen('C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.1\\bin\\pycharm64.exe')
            # os. system("C:\Program Files\JetBrains\PyCharm Community Edition 2021.1.1\bin\pycharm64.exe")
            continue
        
        elif "open remote play" in query:
            speak("Opening PS Remote Play")
            subprocess.Popen('C:\Program Files (x86)\Sony\PS Remote Play\RemotePlay.exe')
            # os. system("C:\Program Files (x86)\Sony\PS Remote Play\RemotePlay.exe")
            continue

        #Only Reply Commands
        
        elif "who are you" in query:
            speak("I am Bagley. Your Personalized Digital Assistant.")
        
        elif "what is the day" in query:
            tellDay()
            continue
        
        elif "what is the time" in query:
            tellTime()
            continue
        
        elif "how are you" in query or "what's up" in query or "what are you doing" in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))
            continue
        
        elif "nothing" in query:
            speak("Oh, Ok")
            exit()
        
        elif "bye" in query:
            speak("Bye. see you later")
            exit()
            
        elif "thank you" in query:
            speak("My pleasure!")
            exit()
        
        elif "thanks" in query:
            speak("your Welcome")
            exit()
        
        elif "exit" in query:
            exit()
        
        elif "stop" in query:
            speak("ok")
            speak("See you later!")
            exit()
        
        elif "thanks bags" in query:
            speak("Your Welcome!")
            speak("by the way i'll be here if you need me. ")
            exit()
        
        elif "search wikipedia" in query:
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia"," ")
            result = wikipedia.summary(query, sentences=20)
            speak(result)
            
        elif "introduce yourself" in query:
            speak("I am Bagley. Your Personalized Assistant")

if __name__ == '__main__':
	Take_query()