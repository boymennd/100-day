from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:/Development\chromedriver.exe"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.get("https://www.instagram.com/")

    def login(self, USER, PASS):
        time.sleep(1)
        time.sleep(1)
        user = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[1]/div/label/input'
        )
        user.send_keys(USER)
        pass_word = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[2]/div/label/input'
        )
        pass_word.send_keys(PASS)
        pass_word.send_keys(Keys.ENTER)
        time.sleep(4)
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/div/section/div/button'
        ).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(
            "/html/body/div[4]/div/div/div/div[3]/button[2]"
        ).click()

    def find_followers(self, KEY_WORD):
        time.sleep(2)
        key_word = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'
        )
        key_word.send_keys(KEY_WORD)
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]'
        ).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]'
        ).click()

    def follow(self):
        time.sleep(2)
        data = self.driver.find_elements_by_css_selector(".PZuss li div div button")
        for item in data:
            time.sleep(1.3)
            if item.text == "Follow":
                item.click()
            else:
                pass
