from bs4 import BeautifulSoup
import requests, lxml

ZILLOW_LINK = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
headers = {
    "Accept-Language": "vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/93.0.148 Chrome/87.0.4280.148 Safari/537.36",
}


class DataInZillow:
    def __init__(self):
        self.response = requests.get(url=ZILLOW_LINK, headers=headers)
        self.dict_zillow = {}
        self.data = BeautifulSoup(self.response.text, "lxml")
        self.find_data()

    def find_data(self):
        link = self.data.find_all(
            name="a", class_="list-card-link list-card-link-top-margin"
        )
        price = self.data.find_all(name="div", class_="list-card-price")
        address = self.data.find_all(name="address", class_="list-card-addr")
        for i in range(len(link)):
            if link[i]['href'][0] == '/':
                href = "https://www.zillow.com" + link[i]['href']
            else:
                href = link[i]['href']
            self.dict_zillow[i] = {
                "address": address[i].text,
                "price": price[i].text,
                "link": href,
            }
