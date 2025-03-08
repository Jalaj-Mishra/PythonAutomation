# Right click

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains

# driver = webdriver.Firefox()


# driver.get(url="https://www.demo.guru99.com/test/simple_context_menu.html")

# driver.maximize_window()

# action = ActionChains(driver=driver)

# button = driver.find_element(by=By.CSS_SELECTOR, value=".context-menu-one.btn.btn-neutral")

# action.context_click(on_element=button).perform()

# copyOption = driver.find_element(by=By.XPATH, value="//*[@id='authentication']/ul/li[3]/span")

# time.sleep(5)
# copyOption.click()
# input("Press enter to exit ...")



#---------------------------------------------------------------------------------------------------------------------------------------#

# Double Click

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Firefox()

driver.get(url="https://www.demo.guru99.com/test/simple_context_menu.html")


driver.maximize_window()


action = ActionChains(driver=driver)

button = driver.find_element(by=By.XPATH, value="//*[@id='authentication']/button")

action.double_click(on_element=button).perform()


time.sleep(5)