# window handles

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(url="https://www.yatra.com")
driver.maximize_window()

main_window = driver.current_window_handle

driver.find_element(by=By.CSS_SELECTOR, value=".swiper-slide.swiper-slide-active.css-1sm4xjg").click()

window_handles = driver.window_handles

for handle in window_handles:
    if handle != main_window:
        driver.switch_to.window(handle)
        driver.find_element(by=By.ID, value="booking_engine_cabs").click()
        time.sleep(10)
        driver.close()
driver.switch_to.window(main_window)
time.sleep(10)

driver.close()