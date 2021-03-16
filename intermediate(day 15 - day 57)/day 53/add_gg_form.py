from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


chrome_driver_path = "C:/Development\chromedriver.exe"
GG_FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSch26L6dfDLi-O5tzXbzxfsYRNIiR1aiW0q7ef5awCawY3kWQ/viewform?usp=sf_link"


class AddGgForm:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.get(url=GG_FORM_LINK)

    def add_form(self, address, price, link):
        time.sleep(2)
        get_address = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
        )
        get_address.send_keys(address)
        get_price = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
        )
        get_price.send_keys(price)
        get_link = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
        )
        get_link.send_keys(link)
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span'
        ).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div[1]/div/div[4]/a"
        ).click()
