
# Project link - https://youtu.be/e9Bf769mXu0?si=-YkQ7Mr4NfouHAA-

# Requirements:

# Open http://www.tutorialsninja.com/demo 
# Select 2 iphones
# Take 1 screenshot
# Select 1 laptop(HP LP3065)
# Select delievery date: 31-12-2026
# Create a Guest account and complete the checkout process
# Print the total price and confirmation message in the console


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# assign webdriver
driver = webdriver.Firefox()

# open url and maximize window
driver.get(url="http://www.tutorialsninja.com/demo/")
driver.maximize_window()

# redirect to the Phones tab
PhoneSection = driver.find_element(by=By.XPATH, value="//a[text()='Phones & PDAs']").click()
time.sleep(2)


# Selecting the iPhone
iPhone = driver.find_element(by=By.XPATH, value="//a[text()='iPhone']").click()
time.sleep(2)

# Selecting the iPhone model
iPhoneDetails = driver.find_element(by=By.XPATH, value="//ul[@class='thumbnails']/li[1]").click()
time.sleep(2)

# saving the images of the product.
for i in range(6):
    driver.save_screenshot(f'project_imgs/iphone_{i}_pic.png')
    arrowKey = driver.find_element(by=By.XPATH, value="//button[@title='Next (Right arrow key)']").click()
    time.sleep(3)

# closing the img frame.
driver.find_element(by=By.XPATH, value="//button[@title='Close (Esc)']").click()
time.sleep(1)


#enter the desired quantity of the product.
driver.find_element(by=By.ID, value="input-quantity").clear()
time.sleep(1)
driver.find_element(by=By.ID, value="input-quantity").send_keys("2")
time.sleep(1)


# adding the product to cart.
AddToCart = driver.find_element(by=By.ID, value="button-cart").click()




# Moving to the Laptops Section
# action = ActionChains(driver=driver)
# action.move_to_element(driver.find_element(by=By.XPATH, value="//ul[@class='nav navbar-nav']/li[2]")).perform()
# option = driver.find_element(by=By.XPATH, value="//a[text()='Show AllLaptops & Notebooks']")
# action.click(on_element=option).perform()



# # Selecting desired laptop
# driver.find_element(by=By.XPATH, value="//a[text()='HP LP3065']").click()
# time.sleep(2)


# driver.find_element(by=By.XPATH, value="//ul[@class='thumbnails']/li[1]/a[@title='HP LP3065']").click()
# time.sleep(2)

# # Saving the screenshots of the products
# for i in range(3):
#     driver.save_screenshot(f'project_imgs/laptop(HP LP3065)_{i}_pic.png')
#     arrowKey = driver.find_element(by=By.XPATH, value="//button[@title='Next (Right arrow key)']").click()
#     time.sleep(2)

# # Closing the img frame.
# driver.find_element(by=By.XPATH, value="//button[@title='Close (Esc)']").click()
# time.sleep(1)



# # adding the product to cart.
# AddToCart = driver.find_element(by=By.ID, value="button-cart").click()

input("Press enter to exit...")
driver.close()

