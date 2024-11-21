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

****Getting Started**

**1.Clone the repository:****

```git clone https://github.com/yourusername/LiveCryptoTracker.git```
```cd LiveCryptoTracker```

**Install the required Python libraries:**

```pip install -r pandas xlwings time requests```

**Run the script:**

```python crypto_analysis.py```

**File Structure**

__**crypto_analysis.py:**_ Main script to fetch, analyze, and update live cryptocurrency data.
_**CryptoLive.xlsx:**_ The Excel file where live data is updated (generated automatically if not present).

**Prerequisites**

Ensure the following are installed:

Python 3.8+
Microsoft Excel (for live updating feature)
Python libraries:
   requests
   pandas
   xlwings

**How It Works**

**Data Fetching:**

The script retrieves data from the CoinGecko API's /coins/markets endpoint.

**Analysis:**
Processes the API data to identify key metrics.

**Excel Integration:**

Updates the Excel sheet every 5 minutes with live data using xlwings.

**License**
This project is licensed under the MIT License. See the LICENSE file for details.
