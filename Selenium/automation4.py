# Drag and Drop in selenium

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



driver = webdriver.Chrome()

driver.get(url="https://the-internet.herokuapp.com/drag_and_drop")

source = driver.find_element(by=By.ID, value="column-a")
target = driver.find_element(by=By.ID, value="column-b")

action = ActionChains(driver=driver)
action.drag_and_drop(source=source, target=target).perform()

time.sleep(5)

driver.close()