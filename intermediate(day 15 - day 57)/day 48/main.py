from selenium import webdriver

chrome_driver_path = "C:/Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org/")
dict_event = {}
# x_part = '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li'
# for i in range(1,5):
#     dict_event[i] = {
#         'time': driver.find_element_by_xpath(f'{x_part}[{i}]/time').text,
#         'name': driver.find_element_by_xpath(f'{x_part}[{i}]/a').text,
#
#     }
# print(dict_event)
data_time = driver.find_elements_by_css_selector(".event-widget time")
data_name = driver.find_elements_by_css_selector(".event-widget li a")
for i in range(len(data_name)):
    dict_event[i + 1] = {
        "time": data_time[i].text,
        "name": data_name[i].text,
    }
print(dict_event)
driver.quit()

# x_part3 = //*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[1]/time
