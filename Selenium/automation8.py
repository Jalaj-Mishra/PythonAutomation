# window handles

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get(url="https://www.yatra.com")
driver.maximize_window()

main_window = driver.current_window_handle

driver.find_element(by=By.CSS_SELECTOR, value=".swiper-slide.swiper-slide-active.css-1sm4xjg").click()


time.sleep(4)

driver.close()