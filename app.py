import streamlit as st
import keyboard
import pickle
import pandas as pd
import os

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

print("\n\nPlease Press Left Shift key watch the output in browser !!! \n\n")
while keyboard.read_key() == 'shift':
    os.system("streamlit run app.py")