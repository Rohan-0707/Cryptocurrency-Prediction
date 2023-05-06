import pyttsx3


def app():
    import streamlit as st
    import keyboard
    import pickle
    from time import sleep
    import pyttsx3
    import speech_recognition as sr
    # import pandas as pd
    import os
    
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    #print(voices[0].id)
    #print(voices)
    engine.setProperty('voice', voices[0].id)
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def load_data():
        with open("data.pkl", "rb") as file:
            data = pickle.load(file)
        return data

    df = load_data()

    def show_data(df):
        st.title("Hello, this is DataFrame1")
        st.write(df)

    show_data(df)

    #This is to run the streamlit command in terminal !!!

    print("\n\nPlease Press Left Shift key watch the output in browser !!! \n")
    while keyboard.read_key() == 'shift':
        speak("Please wait, we are fetching data !")
        sleep(5)
        speak("Yeah, Data Collected !")
        speak("Please wait, Opening predicted data on browser !")
        os.system("streamlit run app.py")
        
def team():
    
    import pyttsx3
    from time import sleep
    import keyboard
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    #print(voices[0].id)
    #print(voices)
    engine.setProperty('voice', voices[0].id)
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()
        
        
    print("\n\n--------------------------- Team RAJ ---------------------------")
    speak("Here is some information about RAJ")
    print("\n\nTeam Leader : Rohan Kumar Bhoi")
    speak("Team Leader, Mister Rohan Kumar Bhoi")
    print("\nDevelopers and Presentors : ")
    speak("Developers and Presentors !")
    print("\n1) Aayan Sattar Mulla")
    speak("First, Mister Ayaan sattaar Mulaa")
    print("2) Jiya Vinod Pardeshi")
    speak("Second, Miss jiyaa vinod paardeshi")

    sleep(2)
    speak("Here is some Information of Mister Rohan Kumar Bhoi !")
    print("\n\n----------------------Mr. Rohan Kumar Bhoi----------------------")
    print("\nName : Rohan Kumar Bhoi")
    print("Age : 19")
    print("City : Pune")
    print("College : Zeal Polytechnic Pune")
    print("Mobile No : +91 7249467380")
    print("Instagram : ceo_rohan_")
    print("Twitter : ceo_rohan_")
    print("Facebook : ceo_rohan")
    print("GitHub : Rohan-0707")

    
    sleep(2)
    speak("Here is some Information of Mister Ayaan sattaar Mulaa !")
    print("\n\n----------------------Mr. Aayan Sattar Mulla----------------------")
    print("\nName : Aayan Sattar Mulla")
    print("Age : 18")
    print("City : Pune")
    print("College : Zeal Polytechnic Pune")
    print("Mobile No : +91 7498464032")
    print("Instagram : ")
    print("Twitter : ")
    print("Facebook : ")
    print("GitHub : ")

    
    sleep(2)
    speak("Here is some Information of Miss jiyaa vinod paardeshi !")
    print("\n\n----------------------Miss. Jiya Vinod Pardeshi----------------------")
    print("\nName : Jiya Vinod Pardeshi")
    print("Age : ")
    print("City : Pune")
    print("College : Zeal Polytechnic Pune")
    print("Mobile No : +91 8421173195")
    print("Instagram : ")
    print("Twitter : ")
    print("Facebook : ")
    print("GitHub : ")

    
    print("")
    print("")
    
    
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# #print(voices[0].id)
# #print(voices)
# engine.setProperty('voice', voices[0].id)
# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()
    
# speak("This project is completed under the guidence of, Professor R H Moollye")