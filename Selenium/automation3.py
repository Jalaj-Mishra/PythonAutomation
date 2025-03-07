#  wait events 




### 1. Static wait - using time.sleep()


# import time
# from selenium import webdriver

# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()

# driver.get(url="https://www.selenium.dev/selenium/web/dynamic.html")

# driver.find_element(by=By.ID, value="adder").click()

# time.sleep(5)

# driver.find_element(by=By.ID, value="box0").click()

# driver.close()

# input("Press enter to exit....")


# -------------------------------------------------------------------------------------------- #

### 2. Dynamic wait - implicit_wait



# from selenium import webdriver

# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()

# driver.get(url="https://www.selenium.dev/selenium/web/dynamic.html")

# driver.implicitly_wait(4)

# driver.find_element(by=By.ID, value="adder").click()


# driver.find_element(by=By.ID, value="box0").click()

# driver.close()

# input("Press enter to exit....")




# -------------------------------------------------------------------------------------------- #

### 2. Dynamic wait - explicit_wait

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

driver.get(url="https://www.selenium.dev/selenium/web/dynamic.html")

driver.find_element(by=By.ID, value="reveal").click()

wait = WebDriverWait(driver=driver, timeout=4)

inputBox = wait.until(EC.visibility_of_element_located(locator=(By.ID, "revealed")))
inputBox.send_keys("Jalaj")