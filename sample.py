import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Nova Sir. Please tell me how may I help you")


def takecommand():
    # it takes input command from the user and returns string output
    query = input("Type your command: ").lower()
    #print(f"User said: {query}\n") 
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'play music' in query:
            webbrowser.open("https://www.youtube.com/watch?v=691Gy98MWbw&list=PLodGlMTHXMfp6SBEdIiFHxHqlbm8ntOmb&ab_channel=Gonzalop")
            
        elif "What's the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
        elif 'open code' in query:
            codePath = "C:\\Users\\aj954\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")
            
        elif 'open telegram' in query:
            webbrowser.open("telegram.com")
            
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
            
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")
            
        elif 'open amazon' in query:
            webbrowser.open("amazon.com")
            
        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")
            
        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            
        elif 'play my best song' in query:
            webbrowser.open("https://www.youtube.com/watch?v=a8CF5YudYUk&list=RDMM5oExKMYIE9U&index=12&ab_channel=DhruvanMoorthy")
            
        elif 'open chrome' in query:
            webbrowser.open("chrome.com")
            
        elif 'email to anuj' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "aj9544390@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend anuj. I am not able to send this email")    
        
