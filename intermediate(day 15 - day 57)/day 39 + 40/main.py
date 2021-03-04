import requests, os, datetime, smtplib
from mail_customer import MailCus
my_mail = "iiobi1907@gmail.com"
pass_mail = os.environ.get("PASS_MAIL")
flight_search_endpoints = "https://tequila-api.kiwi.com/v2/search"
sheety_flight_endpoint = (
    "https://api.sheety.co/3433f1cc0c04e3c800e561ff11e8e9d4/flightDeals/prices"
)
headers = {"apikey": os.environ.get("KEY_FLIGHT_SEARCH")}
USER_sheety = os.environ.get("USER_sheety")
PASS_sheety = os.environ.get("PASS_sheety")
mail_customer = MailCus()
now = datetime.datetime.now()
tomorrow = now + datetime.timedelta(minutes=1440)
date_to = now + datetime.timedelta(minutes=259200)
response1 = requests.get(url=sheety_flight_endpoint, auth=(USER_sheety, PASS_sheety))
data_city = response1.json()["prices"]
for city in data_city:
    parameters = {
        "dateFrom": tomorrow.strftime("%d/%m/%Y"),
        "dateTo": date_to.strftime("%d/%m/%Y"),
        "flight_type": "round",
        "one_for_city": 1,
        "night_in_dst_from": 7,
        "night_in_dst_to": 28,
        "fly_from": "VN",
        "fly_to": city["iataCode"],
        "max_stopovers": 0,
        "curr": "VND",
    }
    response = requests.get(
        url=flight_search_endpoints, params=parameters, headers=headers
    )
    try:
        data_flight = response.json()["data"][0]
        if data_flight["price"] < city["lowestPrice"]:
            date = data_flight["route"][0]["local_departure"].split("T")[0]
            url = f"{sheety_flight_endpoint}/{city['id']}"
            param_put = {"price": {"lowestPrice": data_flight["price"]}}
            requests.put(url=url, json=param_put, auth=(USER_sheety, PASS_sheety))
            for mail_cus in mail_customer.mail_list:
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.login(user=my_mail, password=pass_mail)
                    connection.starttls()
                    connection.sendmail(
                        from_addr=my_mail,
                        to_addrs=mail_cus,
                        msg=f'Subject:Low price alert!\n\nOnly {data_flight["price"]} vnd to fly from {data_flight["cityFrom"]}-{data_flight["flyFrom"]} to {data_flight["cityTo"]}-{data_flight["flyTo"]},from {date}',
                    )
    except:
        pass


# query_endpoint = "https://tequila-api.kiwi.com/locations/query"
# response1 = requests.get(url=sheety_flight_endpoint, auth=(USER_sheety, PASS_sheety))
# data_city = response1.json()['prices']
# for city in data_city:
#     parameters1 = {
#         "apikey":os.environ.get("KEY_FLIGHT_SEARCH"),
#         "term":city['city']
#     }
#     response2 = requests.get(url=query_endpoint,params=parameters1)
#     data = response2.json()['locations'][0]['code']
#     url = f"{sheety_flight_endpoint}/{city['id']}"
#     param_put = {
#         "price":{
#             "iataCode":data
#         }}
#     requests.put(url=url,json=param_put,auth=(USER_sheety,PASS_sheety))
