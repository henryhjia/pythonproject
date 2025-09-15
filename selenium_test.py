"""
 test selenium
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("http://www.saucedemo.com")

username = driver.find_element(By.ID, "user-name").send_keys("standard_user")
password = driver.find_element(By.ID, "password").send_keys("secret_sauce")
login_button = driver.find_element(By.ID, "login-button").click()

time.sleep(5)
print("Page title after login:", driver.title)

menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
menu_button.click()

time.sleep(3)

logout_button = driver.find_element(By.ID, "logout_sidebar_link")
logout_button.click()

time.sleep(3)
print("Page title after logout:", driver.title)

driver.quit()




