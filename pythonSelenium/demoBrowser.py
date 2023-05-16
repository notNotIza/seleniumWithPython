from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#chrome cannot be invoked directly
#1. get the driver where it is
serviceObject = Service("/chromeDriver/chromedriver.exe")
#2. invoke and assign to a variable for referencing later
driver = webdriver.Chrome(service= serviceObject)

#3. try using the browser through the driver... try going to a site
driver.get("https://www.w3schools.com/")

#4. now let's try learning the different commands

## go to https://selenium-python.readthedocs.io/ and navigate to Getting Started
driver.get("https://selenium-python.readthedocs.io/")
##first assert that you are at the page
assert "Selenium with Python" in driver.title
print(driver.current_url)