import os
import requests
import datetime
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
STOCK_API_KEY = "HR0CSGK85IJXAB98"
STOCK_URL = "https://www.alphavantage.co/query"
stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

stock_response = requests.get(url=STOCK_URL, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()
stock_data = stock_data["Time Series (Daily)"]
stock_current = stock_data[list(stock_data)[0]]
print(stock_current)

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
now = datetime.datetime.now()
date = now.date()

NEWS_API_KEY = "e2446da8be2f4a00abac46f2beecf0e1"
NEWS_URL = "https://newsapi.org/v2/everything"
news_parameters = {
    "q": COMPANY_NAME,
    "from": date.__str__(),
    "sortBy": "popularity",
    "apiKey": NEWS_API_KEY,
}

news_response = requests.get(url=NEWS_URL, params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()
news_data = news_data['articles']
news_top = news_data[:3]
print(news_top)


# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
TWILIO_SID = "AC6aca28f106772e6f4a909358a22a1a0f"
TWILIO_AT = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_NUM = "+17652689798"


def get_message(news):
    if stock_current['1. open'] > stock_current['4. close']:
        return f"TSLA: 🔻{float(stock_current['1. open'])-float(stock_current['4. close'])} \nHeadline: " \
               f"{news['title']} \nBrief: {news['description']} \nURL: {news['url']}"
    else:
        return f"TSLA: 🔺{float(stock_current['4. close'])-float(stock_current['1. open'])} \nHeadline: " \
               f"{news['title']} \nBrief: {news['description']} \nURL: {news['url']}"


client = Client(TWILIO_SID, TWILIO_AT)
for news in news_top:
    message = client.messages.create(
      body=get_message(news),
      from_="+17652689798",
      to="+917970940623"
    )
    print(message.sid)

# Optional: Format the SMS message like this:
"""TSLA: 🔺2% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey have 
gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings 
show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash. 
or "TSLA: 🔻5% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey 
have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F 
filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus 
market crash. """
