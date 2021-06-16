'''
Filename: update_product_data.py
Path: /GitHub/hackathon-WIT
Created Date: Thursday, June 10th 2021, 1:31:13 am
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

    recordVideo = 0

    greetUser()

    speechEngine("Do you also want to upload video?")
    query = getAudioData(timeout=5).lower()

    if 'yes' in query :
            recordVideo = 1
            speechEngine("You will be asked to recird video at the end. Please record video and press upload.")

    # get user id based on face data, later to be removed from here and extract directly
    speechEngine("ID")
    id = getAudioData(timeout=None).lower()

    speechEngine("Produce Type")
    queryProd = getAudioData(timeout=None).lower()

    speechEngine("Produce quality")
    queryProdQual = getAudioData(timeout=None).lower()

    speechEngine("Produce Quantity")
    queryProdQt = getAudioData(timeout=None).lower()

    speechEngine("Price for Small amount")
    queryPriceSml = getAudioData(timeout=None).lower()

    speechEngine("Price for Bulk amount")
    queryPriceBlk = getAudioData(timeout=None).lower()

    speechEngine("Expiry days")
    queryExpiry = getAudioData(timeout=None).lower()

    # attributes are based on product
    # can we add them dynamically here
    # take 5 diferent examples
    cFile = pd.read_csv('product_database.csv', encoding='utf-8')
    #print(cFile)
    
    df = pd.DataFrame(cFile)
    print(df)

    num_rec = len(df.axes[0])
    print(".Present number of records: ",num_rec)
    74    ``
    new_row = pd.DataFrame({'ID': id, 'ProduceType': queryProd, 'ProduceQuality':queryProdQual,
                                'ProduceQuantity': queryProdQt, 'PriceSmallQt': queryPriceSml, 
                                'PriceLargeQt': queryPriceBlk, 'ExpiryDate' : }, index=[0])

    df = df.append(new_row, ignore_index=True)
    print(df)
    num_rec = len(df.axes[0])
    print("New number of records: ",num_rec)

    df.to_csv('user_database.csv', index=False)

    if recordVideo == 1:
        #open camera to record video