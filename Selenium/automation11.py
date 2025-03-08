from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get(url="https://www.google.com")

driver.maximize_window()
time.sleep(3)

driver.save_screenshot("screenshot.png")

driver.close()