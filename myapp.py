import yfinance as yf  # Yahoo Finance
import streamlit as st  # Streamlit
import pandas as pd  # Pandas
from datetime import date  # Date 

st.write("""


# Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of Google!

""")
with st.form(key='my_form'):
    tickerSymbol = st.text_input("Enter the stock ticker symbol", 'GOOGL')

    col1, col2 = st.columns(2)
    with col1:
        startDate = st.date_input("Start Date", pd.to_datetime('2024-01-01'))
    with col2:
        endDate = st.date_input("End Date", date.today())
    
    submit_button = st.form_submit_button(label='GO')

if submit_button :
    try:
        
        # Get data on this ticker
        tickerData = yf.Ticker(tickerSymbol)
        # Get the historical prices for this ticker
        tickerDf = tickerData.history(period='1d', start=startDate, end=endDate)
        # Open High Low Close Volume Dividends Stock Splits

        st.line_chart(tickerDf.Close)
        
    except Exception as e:
        st.write("Error fetching data for  {tickerSymblo}")

