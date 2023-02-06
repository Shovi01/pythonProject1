import string

import pyttsx3
import requests
import scipy as sp
from nltk.corpus import stopwords

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

    # def wishme():
    #     hour = int(datetime.datetime.now().hour)
    #     if hour>=0 and hour<12:
    #         speak("Good morning sir")
    #         speak("how may i help you")
    #     elif hour>=12 and hour<18:
    #         speak("good afternoon sir")
    #         speak("how may i help you")
    #     else:
    #         speak("good evening")
    #         speak("how may i help you")


if __name__ == '__main__':

    # speak("good evening sir")
    # speak ("how can i help you")
    import pyttsx3  # pip install pyttsx3
    import speech_recognition as sr  # pip install speechRecognition
    import datetime
    import wikipedia  # pip install wikipedia
    import webbrowser
    import os
    import smtplib

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    engine.setProperty('voice', voices[1].id)


    def speak(audio):
        engine.say(audio)
        engine.runAndWait()


    def wishme():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("Good morning sir")
        elif hour >= 12 and hour < 18:

            speak("good afternoon sir")
           # speak("how may i help you")
        else:
            speak("good evening")
           # speak("how may i help you")

        speak("I am virtual councillor Sir. Please tell me how may I help you")


    def takeCommand():
        # It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            # audio = r.listen(source)
            audio = r.listen(source, 10, 3)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
        return query


    import smtplib, ssl

    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "pk7982@srmist.edu.in.com"
    receiver_email = "prince.mac.march@gmail.com"
    password = input("Type your password and press enter:")
    message = """\
       Subject:Hello sir this is a request from xyz person regarding a appointment."""
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    if __name__ == "__main__":
        wishme()
        while True:
            # if 1:
            query = takeCommand().lower()

            # Logic for executing tasks based on query
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
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'open code' in query:
                codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'email to Shovi' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "princesam0967@@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend Shovi bhai. I am not able to send this email")


                    def open_camera():
                        sp.run('start microsoft.windows.camera:', shell=True)

def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]


def function_preprocess(mess):
    nopunc = []
    for char in mess:
        if char not in string.punctuation:
            nopunc.append(char)
    nopunc = ''.join(nopunc)
    clean = []
    for word in nopunc.split():
        word = word.lower()
        if word not in stopwords.words('english'):
            clean.append(word)
    return clean


from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer as cv
from sklearn.feature_extraction.text import TfidfTransformer

# building our NLP model using naive bayes as classifier
pipeline = Pipeline([('bow', cv(analyzer=function_preprocess)),
                     ('tfidf', TfidfTransformer()),
                     ('classifier', MultinomialNB()),
                     ])
pipeline.fit(data, emotional_class)





