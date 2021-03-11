from bs4 import BeautifulSoup
import requests, lxml, smtplib, os

my_mail = "iobi1907@gmail.com"
pass_mail = os.environ.get("PASS_MAIL")
url = "https://www.amazon.com/dp/B06Y1MP2PY/ref=twister_B087J7MPS4?_encoding=UTF8&th=1"
headers = {
    "Accept-Language": "vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/93.0.148 Chrome/87.0.4280.148 Safari/537.36",
}
response = requests.get(url=url, headers=headers)
data = BeautifulSoup(response.text, "lxml")
data_item = data.find(name="span", id="priceblock_ourprice")
data_name = " ".join(data.find(name="span", id="productTitle").string.split())
item_price = float(data_item.string.split("$")[1])
if item_price < 100:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_mail, password=pass_mail)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs=my_mail,
            msg=f"Subject:Amazon discounts\n\nItems you care in amazon {data_name} discounts only ${item_price}\nThis link:\n{url}",
        )
