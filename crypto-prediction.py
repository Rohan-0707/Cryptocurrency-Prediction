import os
import pandas as pd
import numpy as np
import keyboard
import pyttsx3
from time import sleep

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
#print(voices)
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

import streamlit as st #web app
import matplotlib.pyplot as plt
plt.style.use("fivethirtyeight")

try:
    from binance.spot import Spot as Client

    api_key = "grbtS6aVaMLGqlKjNcRSYSCV6uwuyKEn3zynoSHNFjIodJilIyCI7YD0gbIpUtJI"
    api_secret = "bBru8FTk2LL8jv3AfvYLQQ4kof0ZzMjZKKu1nsSn98hi0bNDw6TxR0yksWFk0rpP"
    client = Client(api_key, api_secret)

    # print(client)

    tickers = ('Bitcoin','Ethereum','Tether','USD Coin','BNB','XRP','Cardano','Binance USD','Solana','Dogecoin','Polkadot','Wrapper Bitcoin','TRON')

    # TODO: add more ticker symbols

    data = client.ticker_price(symbols=['BTCUSDT', 'BNBUSDT', 'ETHUSDT'])

    df = pd.DataFrame.from_dict(data)

    st.title("Crypto Prediction Dashboard")

    st.subheader("using Python! ")

    dropdown = st.multiselect('Pick your Crypto',df.loc[df["symbol"].str.contains("USDT",case=True)][:20])

    st.write('You selected:', dropdown)

    if len(dropdown)>0:

        historical_data = client.klines(dropdown[0], '1d')

        history_df = pd.DataFrame(historical_data)
        history_df.columns=["Open Time" , "Open" , "High" , "Low" , "Close" , "Volume" , "Close Time" , "Quote Asset Vol" , "No. of Trades" , "TB Base Vol" , "TB Quote Vol" , "Ignore"]
        history_df["Open Time"] = pd.to_datetime(history_df["Open Time"]/1000 , unit = "s")
        history_df["Close Time"] = pd.to_datetime(history_df["Close Time"]/1000 , unit = "s")

        num = ["Open", "High", "Low", "Close","Volume"]
        history_df[num] = history_df[num].apply(pd.to_numeric, axis=1)
        history_df.head()

        history_df = history_df[["Open Time", "Open", "High", "Low", "Close","Volume"]]
        indexZeroes = history_df[history_df["Volume"]==0].index
        history_df.drop(indexZeroes , inplace= True)
        history_df.head()
        
        history_df["MA20"] = history_df['Close'][:].rolling(window=5, min_periods=1).mean()
        history_df["MA30"] = history_df['Close'][:].rolling(window=30, min_periods=1).mean()
        history_df["MA60"] = history_df['Close'][:].rolling(window=60, min_periods=1).mean()
        history_df.tail(10)

        def mysig(x):
            if x.MA20<x.MA30<x.MA60:
                return -1
            elif x.MA20>x.MA30>x.MA60:
                return +1
            else:
                return 0

        history_df["signal"] = history_df.apply(mysig, axis=1)
        history_df.tail()

        print(history_df)

        st.line_chart(data=history_df, x="Open Time", y=['Close','MA20', 'MA60'])
        st.bar_chart(data=history_df, x="Open Time", y=['Volume'])
        st.bar_chart(data=history_df, x="Open Time", y=['signal'])

        import plotly.graph_objects as go
        from plotly.subplots import make_subplots
        dfpl = history_df[:518]
        fig = go.Figure(data=[go.Candlestick(x=dfpl.index,
                        open=dfpl['Open'],
                        high=dfpl['High'],
                        low=dfpl['Low'],
                        close=dfpl['Close']),
                        go.Scatter(x=dfpl.index, y=dfpl.MA20, line=dict(color='orange', width=1), name="MA Fast"),
                        go.Scatter(x=dfpl.index, y=dfpl.MA30, line=dict(color='blue', width=1), name="MA Medium"),
                        go.Scatter(x=dfpl.index, y=dfpl.MA60, line=dict(color='black', width=1), name="MA Slow")])

        fig.show()
        
        def trend_alert(df): 
            dfstream = pd.DataFrame(columns=['Open','Close','High','Low'])
            dfstream['Open'] = df['Open'].astype(float)
            dfstream['Close'] = df['Close'].astype(float)
            dfstream['High'] = df['High'].astype(float)
            dfstream['Low'] = df['Low'].astype(float)

            dfstream['MA20'] = dfstream['Open'].rolling(window=20).mean()
            dfstream['MA30'] = dfstream['Open'].rolling(window=30).mean()
            dfstream['MA60'] = dfstream['Open'].rolling(window=60).mean()

            dfstream["signal"] = dfstream.apply(mysig, axis=1)
            dfstream_last_60_vals = dfstream.tail(60) 

            if dfstream_last_60_vals.iloc[59]['signal']==1 and dfstream_last_60_vals.iloc[58]['signal']!=1:
                msg = str("the signal is buying, the Trend is Uptrend")
            elif dfstream_last_60_vals.iloc[59]['signal']==1 and dfstream_last_60_vals.iloc[58]['signal']==1:
                msg = str("the signal is buying, the Trend is Uptrend")    
            elif dfstream_last_60_vals.iloc[59]['signal']==-1 and dfstream_last_60_vals.iloc[58]['signal']==1:
                msg = str("The Trend is changing from Uptrend to Downtrend")     
            elif dfstream_last_60_vals.iloc[59]['signal']==1 and dfstream_last_60_vals.iloc[58]['signal']==-1:
                msg = str("The Trend is changing from Downtrend to Uptrend")
            elif dfstream_last_60_vals.iloc[59]['signal']==-1 and dfstream_last_60_vals.iloc[58]['signal']==-1:
                msg = str("the signal is selling, the Trend is Downtrend")   
            elif dfstream_last_60_vals.iloc[59]['signal']==-1 and dfstream_last_60_vals.iloc[58]['signal']==-1:
                msg = str("the signal is selling, the Trend is Downtrend")   
            else :
                msg = str("No significant trend")
            return msg
        
        trend_alert(history_df[:518])

except:
    speak("Something went wrong !")
    print("\nPlease connect the internet and try to run the program again !!!")
    speak("Please connect the internet and try to run the program again !!!")
    exit()
    

#This is to run the streamlit command in terminal !!!

print("\n\nPlease Press Left Shift key to watch the output in browser !!! \n\n")
# speak("Please Press Left Shift key to watch the output in browser !!!")
while keyboard.read_key() == 'shift':
    speak("Please wait, we are fetching data !")
    sleep(5)
    speak("Yeah, Data Collected !")
    speak("Please wait, Opening predicted data on browser !")
    os.system("streamlit run crypto-prediction.py")