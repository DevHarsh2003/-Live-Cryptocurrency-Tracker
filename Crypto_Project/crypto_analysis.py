import requests
import pandas as pd
import xlwings as xw
import time

def fetch_crypto():
    url="https://api.coingecko.com/api/v3/coins/markets"
    params={
        "vs_currency":"usd",
        "order":"market_cap_desc",
        "per_page":50,
        "page":1
    }
    response=requests.get(url,params=params)
    data=response.json()
    return pd.DataFrame([{
        "Name":coin["name"],
        "Symbol":coin["symbol"],
        "Current Price($)":coin["current_price"],
        "Market Cap":coin["market_cap"],
        "24th Volume":coin["total_volume"],
        "24th Change":coin["price_change_percentage_24h"]
    }for coin in data])

def analyze_data(df):
    top_5_by_market_cap=df.nlargest(5,"Market Cap")
    avg_price=df["Current Price($)"].mean()
    highest_change=df["24th Change"].max()
    lowest_change=df["24th Change"].min()

    print("\nTop 5 Cryptocurrencies By market Cap:")
    print(top_5_by_market_cap)
    print(f"\nAverage Price: ${avg_price:.2f}")
    print(f"\nHighest Change: ${highest_change}%")
    print(f"\nLowest Change: ${lowest_change}%")

def update_excel(df):
    workbook=xw.Book("CryptoLive.xlsx")
    sheet=workbook.sheets[0]
    sheet.range("A1").value=df
    print("Data updated in excel")

def live_update_excel():
    while True:
        df=fetch_crypto()
        update_excel(df)
        print("Excel Updated, waiting for 5 mins...")
        time.sleep(300)

if __name__=="__main__":
    df=fetch_crypto()
    print(df.head)
    analyze_data(df)
    live_update_excel()
