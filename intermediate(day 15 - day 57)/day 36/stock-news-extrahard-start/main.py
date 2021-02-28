import requests, smtplib
from datetime import datetime

my_gmail = "iobi1907@gmail.com"
password = "01214179548"
ALPHA_KEY = "RGEYNX4MX33JCE0Y"
NEW_KEY = "360b646498af4bf9a092aed0574a9604"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
parameters_alpha = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "outputsize": "full",
    "apikey": ALPHA_KEY,
}
parameters_new = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEW_KEY,
}
day = datetime.now().day - 2
response = requests.get("https://www.alphavantage.co/query", params=parameters_alpha)
data = response.json()
data_day = data["Time Series (60min)"]
close_now = float(data_day[f"2021-02-{day} 20:00:00"]["4. close"])

close_yesterday = float(data_day[f"2021-02-{day - 1} 20:00:00"]["4. close"])
price_difference = (close_now - close_yesterday) / close_yesterday * 100
if price_difference > 0:
    tlsa = f"up{round(price_difference,1)}"
else:
    price_difference *= -1
    tlsa = f"down{round(price_difference,1)}"
if price_difference >= 5 or price_difference <= 5:
    response1 = requests.get("https://newsapi.org/v2/everything", params=parameters_new)
    data1 = response1.json()
    data_new = data1["articles"][:3]
    data_send = [f"Headline:{i['title']}\nBrief:{i['description']}" for i in data_new]
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=password)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs=my_gmail,
            msg=f"Subject:Stock volatility TSLA!\n\n{tlsa}\n{data_send}",
        )
