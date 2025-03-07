# frames

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get(url="https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")

driver.maximize_window()
time.sleep(20)
# driver.find_element(by=By.CLASS_NAME, value="user-anonymous tnb-signup-btn w3-bar-item w3-button w3-right ws-green ws-hover-green ga-top ga-top-signup").click()


driver.close()


