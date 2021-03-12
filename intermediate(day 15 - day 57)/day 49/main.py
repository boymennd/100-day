from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:/Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
)
time.sleep(2)
# click to login
driver.find_element_by_css_selector(".cta-modal__primary-btn").click()
time.sleep(2)
# login
driver.find_element_by_id("username").send_keys("boymennd96@gmail.com")
driver.find_element_by_id("password").send_keys("anhcong")
driver.find_element_by_css_selector(".login__form_action_container ").click()
time.sleep(5)
# easy apply
driver.find_element_by_id("ember378").click()
time.sleep(3)
driver.find_element_by_name(
    "urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2436497384,21157002,phoneNumber~nationalNumber)"
).send_keys("123456789")
# send
driver.find_element_by_id("ember385").click()
time.sleep(1)
driver.find_element_by_id("ember385").click()
time.sleep(1)
driver.find_element_by_id(
    "urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2436497384,21157250,numeric)"
).send_keys("1")
time.sleep(1)
driver.find_element_by_css_selector(".fb-radio-buttons span").click()
time.sleep(1)
driver.find_element_by_id(
    "urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2436497384,21157234,numeric)"
).send_keys("0")
driver.find_element_by_id("ember414").click()
time.sleep(1)
driver.find_element_by_id("ember424").click()


# driver.quit()
