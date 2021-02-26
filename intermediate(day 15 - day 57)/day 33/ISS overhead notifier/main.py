import requests, smtplib, time
from datetime import datetime


MY_LAT = 21.061044
MY_LONG = 465.771627
my_gmail = "iobi1907@gmail.com"
password = "01214179548"


def send_mail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=password)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs=my_gmail,
            msg="Subject:ISS are near you\n\nCome out and loot at the ISS",
        )


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

print(iss_latitude)
print(iss_longitude)


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = (int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 7) - 24
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 7

time_now = datetime.now().hour
while True:
    time.sleep(60)
    if time_now < sunrise or time_now > sunset:
        if (
            MY_LAT - 5 < iss_latitude < MY_LAT + 5
            and MY_LONG - 5 < iss_longitude < MY_LONG + 5
        ):
            send_mail()
