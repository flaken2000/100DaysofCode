from twilio.rest import Client
import requests
from datetime import date, timedelta

twilio_account_sid = "your account id"
twilio_auth_token = "your auth token"
twilio_from_number = "number"
twilio_to_number = "number"

STOCK_NAME = "MSFT"
COMPANY_NAME = "Microsoft"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_apikey = "your api key"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_apikey
}

yesterday = str(date.today() - timedelta(days=1))
day_b4_yesterday = str(date.today() - timedelta(days=2))

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_apikey = "your api key"
news_params = {
    "qInTitle": COMPANY_NAME,
    "from": day_b4_yesterday,
    "to": yesterday,
    "sort_by": "relevancy",
    "language": "en",
    "apiKey": news_apikey
}

# Get stock data
response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()
stock_yesterday = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
stock_day_b4_yesterday = float(stock_data["Time Series (Daily)"][day_b4_yesterday]["4. close"])
diff_stock = abs(stock_yesterday - stock_day_b4_yesterday)
diff_perc_stock = round((diff_stock / stock_yesterday) * 100, 1)

if diff_perc_stock >= 1:
    # Get the news
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    news_data = response.json()
    news_3 = news_data["articles"][:3]
    news_items = [{"title": article["title"], "description": article["description"]} for article in news_3]

    if stock_yesterday >= stock_day_b4_yesterday:
        arrow = "🔺"
    else:
        arrow = "🔻"

    # Send text messages
    client = Client(twilio_account_sid, twilio_auth_token)

    for news in news_items:
        twilio_body = (f"{STOCK_NAME}: {arrow}{abs(diff_perc_stock)}%\n"
                       f"Headline: {news["title"]}\n"
                       f"Brief: {news["description"]}")
        message = client.messages.create(from_=twilio_from_number, body=twilio_body, to=twilio_to_number)
