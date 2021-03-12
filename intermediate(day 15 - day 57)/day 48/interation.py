from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")
# x_path = '//*[@id="articlecount"]/a[1]'
# data = driver.find_element_by_xpath(xpath=x_path)
# data = driver.find_element_by_link_text("History")
# data.click()
fname = driver.find_element_by_name("fName")
fname.send_keys("boymennd")
lname = driver.find_element_by_name("lName")
lname.send_keys("congxp1996")
email = driver.find_element_by_name("email")
email.send_keys("iobi1907@gmail.com")
email.send_keys(Keys.ENTER)


# driver.quit()
