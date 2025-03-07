# uploading a file using selenium.  

from selenium import webdriver

from selenium.webdriver.common.by import By



driver = webdriver.Firefox()
driver.get(url="https://the-internet.herokuapp.com/upload")
driver.find_element(by=By.ID, value="file-upload").send_keys("d:\\n.txt")
driver.find_element(by=By.ID, value="file-submit").click()


input("Press enter to exit....")