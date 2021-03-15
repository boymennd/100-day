from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:/Development\chromedriver.exe"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver_speed = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver_twitter = None
        self.down = 0
        self.up = 0
        self.get_internet_speed()

    def get_internet_speed(self):
        self.driver_speed.get("https://www.speedtest.net/")
        self.driver_speed.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]'
        ).click()
        time.sleep(50)
        self.down = float(
            self.driver_speed.find_element_by_xpath(
                '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
            ).text
        )
        self.up = float(
            self.driver_speed.find_element_by_xpath(
                '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span'
            ).text
        )

    def tweet_at_provider(self, message):
        self.driver_twitter = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver_twitter.get("https://twitter.com/")
        time.sleep(2)
        self.driver_twitter.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div/span/span'
        ).click()
        time.sleep(1)
        self.driver_twitter.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
        ).send_keys("boymennd")
        login = self.driver_twitter.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
        )
        login.send_keys("congxp1996")
        login.send_keys(Keys.ENTER)
        time.sleep(3)
        send_message = self.driver_twitter.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div'
        )

        send_message.send_keys(message)
        self.driver_twitter.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div/span/span'
        ).click()
