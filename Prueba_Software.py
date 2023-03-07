from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Firefox()
driver.get("https://www.thefreedictionary.com/")


login = driver.find_element(By.CLASS_NAME, "login-button")
login.click()
time.sleep(2)

login1 = driver.find_element(By.ID,"usrName")
login1.click()
login1.send_keys("andersonvalencia23j@gmail.com")
time.sleep(0.5)

password = driver.find_element(By.ID, "usrPwd")
password.click()
password.send_keys("pruebas123")
time.sleep(0.5)


sumit = driver.find_element(By.NAME, "submit").click()
sumit.send_keys(Keys.RETURN)
time.sleep(1)


driver.close()
