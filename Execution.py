import datetime
from time import sleep
import pyttsx3
import webbrowser
import speech_recognition as sr
import os
from pynput.keyboard import *  #To control Runtime controls like menu
import keyboard

# key = msvcrt.getch().lower() #To detect the key !

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
#print(voices)
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning  !")

    elif hour>=12 and hour<18:
        speak("Good Afternoon  !")

    else:
        speak("Good Evening  !")
        

wishme()
print("\nWelcome to Zeal Polytechnic Pune !")
speak("Welcome to Zeal Polytechnic Pune !")
    
print("\nMy Name is Jarvis !")
speak("My Name is Jarvis !")
print("I would like to introduce my self !")
speak("I would like to introduce my self !")

print("\nI was developed by Mr.Rohan Kumar Bhoi")
speak("I was developed by Mister Rohan Kumar Bhoi !")
print("\nPage of Mr.Rohan : https://ceorohan.blogspot.com")
print("\nThis is a project of Final Year !")
speak("This is a project of Final Year !")

speak("Let me introduce this project now !")

print("\nTeam RAJ...")
print("\nR : Rohan Kumar Bhoi")
print("A : Aayan Sattar Mulla")
print("J : Jiya Vinod Pardeshi")
speak("This Project is developed by Team R A J (RAJ)")
speak("This project is helpful for specially traders, to predict the stock prices !")
print("\nGuided by Prof. R. H. Mule")
speak("The project is completed under the guidence of, Professor R H Moollye !")
speak("Moving towards, I would like to know you,")

#print("I am would be able to predict the data regarding to the cryptocurrency, such as Prediction of Stock Price !")
speak("This project are able to predict the data regarding to the cryptocurrency, such as Prediction of Stock Price !")
print("\nPlease choose a option from the given menu to continue !")
speak("Please choose a option from the given menu to continue !")

print("\n\n-----------------------------Menu-----------------------------\n\n")
print("Press 1 to watch the recent data in the form of Table !")
speak("Press 1 to watch the recent data in the form of Table !")

print("\nPress 2 to watch the predicted data in the form of statistics !")
speak("Press 2 to watch the predicted data in the form of statistics !")

print("\nPress 3 to know about our team !")
speak("Press 3 to know about our team !")

print("\nPress any other key to Exit the Program !")
speak("Press any other key to Exit the Program !")

print("\n\n---------------------------------------------------------------\n\n")

if keyboard.read_key() == '1':
    os.system("cls")
    print("\n\nYou selected fisrt option, Working on recent data !")
    speak("You selected fisrt option, Working on recent data !")
    os.system("cls")
    try:
        os.system('C:/Users/rohan/AppData/Local/Programs/Python/Python311/python.exe "d:/Final Year PROJ/Projects/FinalYearProject/crypto-prediction/datafile.py"')
        from Project import app
        app()
    
    except:
        print("\n\nError Occured !")
    
elif keyboard.read_key() == '2':
    os.system("cls")
    try:
        print("\n\nGood ! You selected second option, please wait a while...")
        speak("Good ! You selected second option, please wait a while !")
        os.system('C:/Users/rohan/AppData/Local/Programs/Python/Python311/python.exe "d:/Final Year PROJ/Projects/FinalYearProject/crypto-prediction/crypto-prediction.py"')
    except:
        print("\n\nError Occured !")

elif keyboard.read_key() == '3':
    speak("You have selected third Option, wait, we are fetching teams information from Google !")
    sleep(3)
    os.system("cls")
    from Project import team
    team()
    sleep(7)
    speak("Due to the command line interrupts, we are unable to start over the program !")
    speak("Would you like to run the program again from start ?")
    speak("Press Y for Yes or N for No !")
    if keyboard.read_key() == 'y':
        speak("Running Program Again !")
        os.system('C:/Users/rohan/AppData/Local/Programs/Python/Python311/python.exe "d:/Final Year PROJ/Projects/FinalYearProject/crypto-prediction/Execution.py"')
    
else:
    speak("Run the program again to continue !")
    sleep(2)
    print("\nWould you like to visit the page of zeal polytechnic ?")
    speak("Would you like to visit the page of, zeal polytechnic ?")
    print("\nPress Y for Yes and N for No !")
    speak("Press Y for Yes and N for No !")
    if keyboard.read_key() == 'y':
        speak("Opening Zeal's Page on Browser !")
        webbrowser.open("https://zealpolytechnic.com/")
    else:
        print("\nShutting Down...!")
        speak("Shutting Down...........!")
        sleep(5)
        print("\nShutdown Successful !\n\n")
        sleep(3)
        
os.system("cls")

sleep(5)
print("\n\nIf you want to run the program again, Please press Left Shift Key !")
speak("If you want to run the program again, Please press Left Shift Key !")

if keyboard.read_key() == 'shift':
    speak("Okay, running program again from start !")
    os.system("cls")
    os.system('C:/Users/rohan/AppData/Local/Programs/Python/Python311/python.exe "d:/Final Year PROJ/Projects/FinalYearProject/crypto-prediction/Execution.py"')
    
else:
    speak("Okay, Good Bye !!!")
    print("\n\n------------------ Have a Nice Day ------------------")
    speak("Have a Nice Day !!!")