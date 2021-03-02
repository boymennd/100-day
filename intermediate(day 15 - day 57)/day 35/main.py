import requests, smtplib,os

my_gmail = "iobi1907@gmail.com"
password = os.environ.get("PASS_MAIL")
MY_LAT = 21.027763
MY_LONG = 105.834160
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily,alerts",
    "appid": WEATHER_API_KEY,
}
response = requests.get(
    "https://api.openweathermap.org/data/2.5/onecall", params=parameters
)
response.raise_for_status()
data = response.json()
hourly = data["hourly"][7:19]
will_rain = False
for hour in hourly:
    id = hour["weather"][0]["id"]
    if id > 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=password)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs=my_gmail,
            msg="Subject:It wil rain\n\nBe careful when it rains, bring an umbrella",
        )
