# Live-Cryptocurrency-Tracker

**Overview**

This project fetches live data for the top 50 cryptocurrencies by market capitalization using the CoinGecko API. The data is analyzed and displayed in a live-updating Excel sheet, providing real-time insights into cryptocurrency trends.

**Features**

1. Fetches real-time data for the top 50 cryptocurrencies, including:

   Cryptocurrency Name

   Symbol

   Current Price (USD)

   Market Capitalization

   24-hour Trading Volume

   24-hour Percentage Price Change

2. Analyzes key metrics:

   Identifies the top 5 cryptocurrencies by market capitalization.

   Calculates the average price of the top 50 cryptocurrencies.

   Tracks the highest and lowest 24-hour percentage price changes.

3. Updates an Excel sheet (CryptoLive.xlsx) every 5 minutes using the xlwings library.
