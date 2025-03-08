# handling iframes

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get(url="https://www.tutorialspoint.com/selenium/practice/frames.php")

driver.maximize_window()

frames = driver.find_elements(by=By.TAG_NAME, value="iframe")

print(len(frames))

driver.switch_to.frame(0)

text = driver.find_element(by=By.TAG_NAME, value="h1")

print(text.text)



input("Press Enter to exit ...")


