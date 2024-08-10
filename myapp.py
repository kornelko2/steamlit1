import yfinance as yf  # Yahoo Finance
import streamlit as st  # Streamlit
import pandas as pd  # Pandas

st.write("""


# Simple Stock Price App

Shown are the stock closing price and volume of Google!

""")

# Define the ticker symbol and the data source
tickerSymbol = 'GOOGL'
# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2020-5-31', end='2024-5-31')
# Open High Low Close Volume Dividends Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

