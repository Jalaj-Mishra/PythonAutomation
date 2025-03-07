# Interaction and Navigation commands



from selenium import webdriver

driver = webdriver.Chrome()

driver.get(url="https://www.youtube.com")


# interaction commands   -  title, current_url

title = driver.title
currentUrl=driver.current_url
print(title, currentUrl)



driver.get(url="https://www.google.com")

title = driver.title
currentUrl=driver.current_url
print(title, currentUrl)



# Navigation commands  - back(), forward()

driver.back()
title = driver.title
currentUrl=driver.current_url
print(title,currentUrl)


driver.forward()
title = driver.title
currentUrl=driver.current_url
print(title,currentUrl)