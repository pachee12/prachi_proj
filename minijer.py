import pyttsx3 #pip install pyttsx
import datetime
import speech_recognition as sr
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5') #to take voice
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices', voices[0].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("wish you a very good morning ")
    elif hour>=12 and hour<18:
        speak(" good afternoon ")
    else:
        speak("good evening ")
        
    speak("hello  , I am mini jer your personal chat bot, please tell me how may i help you.")


def takecommand():
    #takes microphone command input and returns string output
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
        speak("Say that again please...")  
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 535)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', ' password ')
    server.sendmail('youremail@gmail.com', to, content)     
    server.close()

if __name__ == "__main__":
    #speak("hey prachi")
    wishme()
    while True: #logic for executing task
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'instagram' in query:
            webbrowser.open("instagram.com")  

        elif 'facebook' in query:
            webbrowser.open("facebook.com")  

        elif 'linkdin' in query:
            webbrowser.open("linkdin.com")  

        elif 'google' in query:
            webbrowser.open("google.com")  

        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  

        #elif ' music' in query:
           # music_dir = 'D:\\'
                                     
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'code' in query:
            codepath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)       

        elif 'whatsapp' in query:
            wcodepath = "C:\\Users\\user\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(wcodepath) 
   
        elif 'telegram' in query:
            tcodepath = "C:\\Users\\user\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(tcodepath) 

        elif 'send email' in query :
            try:
                speak("What should I say?")
                content = takecommand()
                to = "email@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email at the moment")       

        elif 'quit' in query:
            exit()      