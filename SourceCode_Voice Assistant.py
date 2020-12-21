import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from webbot import Browser
from selenium import webdriver




emails = {"give multiple emails"}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    '''this function is for speaking '''
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''This function is for the greeting purpose'''
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternood!")

    else:
        speak("Good Evening!")
    speak("I am Jarvis. Please tell me how may i help you?")

def takeCommand():
    '''this function takes microphone input from the user and returns string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that agian please...")
        return "None"
    return query

def sendEmail(to,content):
    '''pehle less secure apps ko enable krna hai jis email se hm bhej rhe honge..google pr dekhlena kaise hota hai'''
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('give email', 'give password')
    server.sendmail('give email', to, content)
    server.close()

if __name__ == '__main__':
    wishMe()
    while True:
        querry = takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in querry:
            speak('Searching wikipedia...')
            querry = querry.replace("wikipedia", "")
            results = wikipedia.summary(querry, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in querry:
            webbrowser.open("youtube.com")

        elif 'open google' in querry:
            webbrowser.open("google.com")

        elif 'open whatsapp' in querry:
            webbrowser.open("https://web.whatsapp.com/")

        elif 'open blackboard' in querry:

            driver = Browser()
            # opening the url
            driver.go_to('https://learn.upes.ac.in/')
            # taking the credentials and loging in
            driver.type('give id', into='USERNAME', id='user_id')
            driver.type('give password', into='PASSWORD', id='passwordFieldId')
            driver.click('LOGIN', tag='span', id='entry-login')
            # cureentTime = datetime.datetime.now().strftime("%H:%M:%S")
            driver.click('OK', tag='button', id = 'agree_button', classname='button-1')
            driver.go_to('https://learn.upes.ac.in/webapps/blackboard/execute/modulepage/view?course_id=_44477_1&cmp_tab_id=_117077_1&mode=view')
            driver.go_to('https://learn.upes.ac.in/webapps/blackboard/content/contentWrapper.jsp?course_id=_44477_1&displayName=Blackboard%20Collaborate%20Ultra%20UPES-CCE&href=%2Fwebapps%2Fblackboard%2Fexecute%2Fblti%2FlaunchPlacement%3Fblti_placement_id%3D_22_1%26course_id%3D_44477_1%26mode%3Dview%26wrapped%3Dtrue')
            # web.click('Cloud Security &amp; Management.BT-CSE-SPZ-CCVT-V-B1.BT-CSE-SPZ-CCVT-V-B2.VR_B_331 – Course Room', tag='button', id='session-f041e5fdeac744b2b83e2cfd78ab3211')
            print("here")
            driver.find_element_by_name('Courses').click()
            # web.click('Cloud Security &amp; Management.BT-CSE-SPZ-CCVT-V-B1.BT-CSE-SPZ-CCVT-V-B2.VR_B_331 – Course Room', tag='div', classname='')
            # web.click('Cloud Security &amp; Management.BT-CSE-SPZ-CCVT-V-B1.BT-CSE-SPZ-CCVT-V-B2.VR_B_331 – Course Room', tag='span', classname='item-list__item-details')
            # web.click('Join Course Room', tag='button', classname='loading-button__icon ng-scope ng-isolate-scope')
            # web.click('Cloud Security &amp; Management.BT-CSE-SPZ-CCVT-V-B1.BT-CSE-SPZ-CCVT-V-B2.VR_B_331 – Course Room', tag='button', id = 'session-f041e5fdeac744b2b83e2cfd78ab3211', classname='session-list-item-content')
            print("also")
            # web.click('Join Course Room', tag='span', id = 'session.course-room.launch-session', classname='ng-scope')
            # web.go_to('https://au.bbcollab.com/collab/ui/session/join/a5e97f1cb41a4179927ecd1fcd2d1941')
            # web.go_to('https://au.bbcollab.com/collab/ui/session/join/350e71f113d54d4cab48fb0e1c0a805f')
            # web.go_to('https://au.bbcollab.com/collab/ui/session/join/33a167fdec334fd6ad8fe1ba3d0600e6')


        elif 'play music' in querry:
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0])) #yaha pr hm randam no. generate kr k usse frr random song bhi play kara skte hai..krna ho to krlena

        elif 'the time' in querry:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in querry:
            codePath = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
            os.startfile(codePath)

        elif 'send email' in querry:
            try:
                # speak("what should I say")
                # content = takeCommand()
                # to = "mishranishi02@gmail.com"
                # sendEmail(to, content)
                # speak("Email has been sent")
                speak("Who do you want to send the email")
                mailto = takeCommand()
                for key in emails:
                    # print(key)
                    # print(mailto)
                    if key.lower() == mailto.lower():
                        to = emails[key]
                        # print(to)
                        speak("What should I say?")
                        content = takeCommand()
                        sendEmail(to, content)
                        speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")

        elif 'quit' in querry:
            break

            # mail search krna