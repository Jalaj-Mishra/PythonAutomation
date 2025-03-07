from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()

driver.get(url="https://www.flipkart.com/")


hover = driver.find_element(by=By.CSS_SELECTOR, value=".H6-NpN._3N4_BX")

actions = ActionChains(driver=driver)
actions.move_to_element(hover).perform()
driver.find_element(by=By.CSS_SELECTOR, value="._1jKL3b").click()

input("Press Enter to exit...")