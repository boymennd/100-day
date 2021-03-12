from selenium import webdriver
import time

chrome_driver_path = "C:/Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element_by_id("cookie")
ids = driver.find_elements_by_css_selector("#store div")
list_id = [item.get_attribute("id") for item in ids]
print(list_id)
data = driver.find_elements_by_css_selector("#store b")
price_list = []
# for item in data:
#     if item.text != "":
#         price_list.append(int(item.text.split("-")[1].replace(",","")))
# print(price_list)
time_out = time.time() + 1
time_end = time.time() + 300
a = 0
while True:
    cookie.click()
    if time.time() > time_out:
        a += 1
        money = int(driver.find_element_by_id("money").text.replace(",", ""))
        cookie_second = float(driver.find_element_by_id("cps").text.split(":")[1])
        data = driver.find_elements_by_css_selector("#store b")
        price_list = []
        for item in data:
            if item.text != "":
                price_list.append(int(item.text.split("-")[1].replace(",", "")))
        id_price = ""
        for i in range(len(price_list)):
            if money > price_list[i]:
                id_price = list_id[i]
        driver.find_element_by_id(id_price).click()
        time_out = time.time() + a
