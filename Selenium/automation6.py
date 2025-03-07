# How to handle Alerts and pop-ups  

# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. alert-type1 which appear right after clicking on source button


from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get(url="https://demoqa.com/alerts")


driver.find_element(by=By.ID, value="alertButton").click()
alert = driver.switch_to.alert

alert.accept()


driver.close()




# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. alert-type2 which appear after 5 seconds when user is clicking on source button

# import time

# from selenium import webdriver
# from selenium.webdriver.common.by import By


# driver = webdriver.Firefox()
# driver.get(url="https://demoqa.com/alerts")


# driver.find_element(by=By.ID, value="timerAlertButton").click()
# time.sleep(5)
# alert = driver.switch_to.alert


# alert.accept()


# driver.close()



# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. alert-type3 which is a confirmation button in which you can select either "ok" or "cancel" option.


# import time

# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Firefox()

# driver.get(url="https://demoqa.com/alerts")

# driver.find_element(by=By.ID, value="confirmButton").click()

# alert = driver.switch_to.alert

# alert.accept()

# driver.close()




# ---------------------------------------------------------------------------------------------------------------------------------------
# 4. alert-type4 which is prompt type alert in which you can enter value


# import time

# from selenium import webdriver

# from selenium.webdriver.common.by import By


# driver = webdriver.Firefox()

# driver.get(url="https://demoqa.com/alerts")

# driver.find_element(by=By.ID,value="promtButton").click()

# alert = driver.switch_to.alert

# alert.send_keys("Jalaj")


# time.sleep(4)
# alert.accept()
# driver.close()