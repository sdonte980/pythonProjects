from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chromeDriver = "/home/oem/PycharmProjects/pythonProject/automation test practi/chromedriver"
driver = webdriver.Chrome(chromeDriver)
driver.get("https://google.co.il")
search = driver.find_element_by_name("q")
search.send_keys("moodle ruppin")
search.send_keys(Keys.ENTER)
print(driver.title)
RuppinMod = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div[1]/a').click()
print(driver.title)
RmUserName = driver.find_element_by_name("username")
RmUserName.click()
RmUserName.send_keys("111111111")
RmPassword = driver.find_element_by_name("password")
RmPassword.click()
# print("Typed Wrong Password")
RmPassword.send_keys("L2pgzil")
time.sleep(32)
RupModConnect = driver.find_element(By.XPATH, '//*[@id="loginbtn"]')

#L2pgzil
#RupModConnect.submit()
RupModConnect.click()
time.sleep(3)


driver.quit()
