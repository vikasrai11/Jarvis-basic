import datetime
from email import message
import webbrowser
import pyttsx3
import speech_recognition
import requests
from requests import get
from bs4 import BeautifulSoup
import os
import pyautogui
import random
from plyer import notification
from pygame import mixer
import speedtest
import pywhatkit as kit



from INTRO import play_gif
play_gif
pyautogui.sleep(1)

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query




if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can call me anytime")
                    break 
                
               

                elif "schedule my day" in query:
                    tasks = [] 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%I:%M %p")
                    speak(f"Time is {strTime}")
                elif "date" in query:
                    strDate=datetime.datetime.now().strftime("%m/ %d/ %y")
                    speak(f"Date is {strDate}")

                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                    )
                

                elif "open" in query:   
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)

                    pyautogui.press("enter")      

                elif 'ip address' in query:
                    ip= get('https://api.ipify.org').text
                    print(f"Your IP address is {ip}")
                    speak(f"your IP address is {ip}")                 
                     
                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576        
                    download_net = wifi.download()/1048576
                    print(f"Wifi download speed is {download_net} MBPS")
                    print(f"Wifi download speed is {download_net} MBPS")
                    speak(f"Wifi download speed is {download_net} MBPS")
                    speak(f"Wifi Upload speed is {upload_net} MBPS")
                    


                # elif "ipl score" in query:
                #     from plyer import notification  
                #     import requests 
                #     from bs4 import BeautifulSoup 
                #     url = "https://www.cricbuzz.com/"
                #     page = requests.get(url)
                #     soup = BeautifulSoup(page.text,"html.parser")
                #     team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                #     team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                #     team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                #     team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                #     a = print(f"{team1} : {team1_score}")
                #     b = print(f"{team2} : {team2_score}")

                #     notification.notify(
                #         title = "IPL SCORE :- ",
                #         message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                #         timeout = 15
                #     )
                
                

                elif "screenshot" in query:
                     import pyautogui 
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")

                # elif "click my photo" in query:
                #     pyautogui.press("super")
                #     pyautogui.typewrite("camera")
                #     pyautogui.press("enter")
                #     pyautogui.sleep(2)
                #     speak("SMILE")
                #     pyautogui.press("enter")k

                
                

               
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                
                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=S980-z1qx3g")
                    elif b==2:
                        webbrowser.open("https://www.youtube.com/watch?v=AETFvQonfV8")
                    elif b==3:
                        webbrowser.open("https://www.youtube.com/watch?v=wjxllfY-GgE")

                elif 'play a song on youtube' in query:
                    speak("Which song would you listen?")
                    query = takeCommand().lower()
                    kit.playonyt({query})

                elif 'open stack overflow' in query:
                    webbrowser.open("www.stackoverflow.com")
                elif 'instagram profile' in query or 'profile on instagram' in query:
                    speak("Enter username to search")
                    name=input("Enter username: ")
                    webbrowser.open(f"www.instagram.com/{name}")
                    

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                


                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)


                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()


                elif "whatsapp message" in query:
                    from Whatsapp import sendMessage
                    sendMessage()

                

                elif "temperature" in query:
                    search = "temperature in mumbai"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

                
                           
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
                elif "finally sleep" in query:
                    speak("Going to sleep,sir")
                    exit()

                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to remember that" + remember.read())

                elif "shutdown system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break

                




                


 