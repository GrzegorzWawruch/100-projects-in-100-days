import requests
import datetime
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "YP7HMAX9406TPKDX"
NEWS_API_KEY = "e840418e15fa4738aae033e3b180149b"
ALPHA_VANTAGE_URL = "https://www.alphavantage.co/query"
NEWS_API_URL = "https://newsapi.org/v2/everything"
twilio_number = "<number>"
my_number = "<number>"
account_sid = "<account_sid>"
auth_token = "<auth_token>"

company = "Tesla"

stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : "IBM",
    "apikey" : STOCK_API_KEY,
}

news_params = {
    "apiKey" : "e840418e15fa4738aae033e3b180149b",
    "q" : company

}

today_data = datetime.date.today()
yesterday_data = today_data - datetime.timedelta(days=1)
one_day_before_yesterday_data = yesterday_data - datetime.timedelta(days=1)

today_data_str = today_data.strftime("%Y-%m-%d")
print(today_data_str)
yesterday_data_str = yesterday_data.strftime("%Y-%m-%d")
print(yesterday_data_str)
one_day_before_yesterday_data_str = one_day_before_yesterday_data.strftime("%Y-%m-%d")
print(one_day_before_yesterday_data_str)

stock_response = requests.get(ALPHA_VANTAGE_URL, params=stock_params)
stock_data = stock_response.json()

news_response = requests.get(NEWS_API_URL, params=news_params)
news_data = news_response.json()
print(news_data)
last_company_news_author =news_data["article"][0]["author"]
last_company_news_title =news_data["article"][0]["title"]
last_company_news_description =news_data["article"][0]["description"]
last_company_news_content =news_data["article"][0]["content"]

stock_price_one_day_before_yesterday = int(stock_data['Time Series (Daily)'][one_day_before_yesterday_data_str]["4. close"])
stock_price_yesterday = int(stock_data['Time Series (Daily)'][yesterday_data_str]["1. open"])
stock_price_difference = stock_price_yesterday - stock_price_one_day_before_yesterday
if stock_price_difference < 0:
    percent_stock_price_difference = round((-(stock_price_difference) / stock_price_one_day_before_yesterday) , 2)
    if percent_stock_price_difference < 0.95:
        proxy_client = TwilioHttpClient()
        proxy_client.session.proxies = {"https": os.environ['https_proxy']}

        client = Client(account_sid, auth_token, http_client=proxy_client)
        message = client.messages \
            .create(
            body="It is going to rain today. Remember to bring an umbrella",
            from_=twilio_number,
            to=my_number,
        )
        print(message.status)
elif stock_price_difference > 0:
    percent_stock_price_difference = round((stock_price_difference) / stock_price_one_day_before_yesterday, 2)
    if percent_stock_price_difference < 0.95:
        proxy_client = TwilioHttpClient()
        proxy_client.session.proxies = {"https": os.environ['https_proxy']}

        client = Client(account_sid, auth_token, http_client=proxy_client)
        message = client.messages \
            .create(
            body=f"Author: {last_company_news_author} \n"
                 f"Title: {last_company_news_title} \n"
                 f"Description: {last_company_news_description} \n"
                 f"{last_company_news_content}",
            from_=twilio_number,
            to=my_number,
        )
        print(message.status)
