from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:/Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://tinder.com")

time.sleep(3)
driver.find_element_by_xpath(
    '//*[@id="t-429325247"]/div/div[2]/div/div/div[1]/button'
).click()

# Login tinder

time.sleep(1)
driver.find_element_by_xpath(
    '//*[@id="t-429325247"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button'
).click()
time.sleep(3)
try:
    driver.find_element_by_xpath(
        '//*[@id="t--1610880557"]/div/div/div[1]/div/div[3]/span/div[2]/button'
    ).click()
except NoSuchElementException:
    driver.find_element_by_xpath(
        '//*[@id="t--1610880557"]/div/div/div[1]/div/div[3]/span/button'
    ).click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="t--1610880557"]/div/div/div[1]/div/div[3]/span/div[2]/button'
    ).click()
else:
    time.sleep(3)
    base_window = driver.window_handles[0]
    fb_window = driver.window_handles[1]
    driver.switch_to.window(fb_window)
    driver.find_element_by_xpath('//*[@id="email"]').send_keys("0979013760")
    driver.find_element_by_xpath('//*[@id="pass"]').send_keys("123456ab")
    driver.find_element_by_xpath('//*[@id="pass"]').send_keys(Keys.ENTER)
    time.sleep(5)
    driver.switch_to.window(base_window)
    driver.find_element_by_xpath(
        '//*[@id="t--1610880557"]/div/div/div/div/div[3]/button[1]'
    ).click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="t--1610880557"]/div/div/div/div/div[3]/button[1]'
    ).click()
    time.sleep(7)
    for i in range(10):
        like = driver.find_element_by_xpath('.//*[@id="Tinder"]/body').send_keys(
            Keys.RIGHT
        )
        time.sleep(2)


# driver.quit()
