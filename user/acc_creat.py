'''
Filename: acc_creat.py
Path: /GitHub/hackathon-WIT
Created Date: Wednesday, June 9th 2021, 11:25:38 pm
Author: Ravi Shekhar Singh

Copyright (c) 2021
'''

import pyttsx3  
import speech_recognition as sr  # pip install pyttsx3
import datetime
import os
import pandas as pd

# Libraries to install
# pip install pyttsx3
# pip install pyttsx3
# pip install pipwin
# pipwin install pyaudio


def speechEngine(audio):
    engine.say(audio)
    engine.runAndWait()


def greetUser():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speechEngine("Good Morning!")

    elif hour >= 12 and hour < 18:
        speechEngine("Good Afternoon!")

    else:
        speechEngine("Good Evening!")

    speechEngine("Welcome to Connect for Good. I am an account bot and I am here to assist you with account creation")


def getAudioData(timeout):

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.0
        audio = r.listen(source,timeout=1,phrase_time_limit=10)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Speech recorded: {query}\n")

    except Exception:
        # print(e)
        print("Speech not recorded. Please say again.")
        return "None"
    return query


def inc(i):
    i=i+1


if __name__ == "__main__":

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    greetUser()

    query = getAudioData(timeout=5).lower()

    if 'open account' in query or "what details" in query:
            speechEngine("I will need your name, contact details, address, location, preferred language, type of goods produced")

    # create a unique account id based on face and add all these data to that
    
    speechEngine("What is your name")
    queryName = getAudioData(timeout=None).lower()

    speechEngine("What is your Contact details")
    queryCont = getAudioData(timeout=None).lower()

    speechEngine("What is your Address")
    queryAddr = getAudioData(timeout=None).lower()

    speechEngine("What is your location")
    queryLoca = getAudioData(timeout=None).lower()

    speechEngine("What is your produce")
    queryProd = getAudioData(timeout=None).lower()

    cFile = pd.read_csv('user_database.csv', encoding='utf-8')
    #print(cFile)
    
    df = pd.DataFrame(cFile)
    print(df)

    num_rec = len(df.axes[0])
    print("Present number of records: ",num_rec)
    new_row = pd.DataFrame({'Name': queryName, 'Contact': queryCont, 'Address':queryAddr,
                                'Location': queryLoca, 'Produce': queryProd}, index=[0])

    df = df.append(new_row, ignore_index=True)
    print(df)
    num_rec = len(df.axes[0])
    print("New number of records: ",num_rec)

    df.to_csv('user_database.csv', index=False)