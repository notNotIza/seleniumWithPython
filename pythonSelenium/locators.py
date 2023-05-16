from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#chrome webdriver
serviceObject  = Service("/chromeDriver/chromedriver.exe")
driver = webdriver.Chrome(service= serviceObject)

driver.get("https://selenium-python.readthedocs.io/")

# try locating certain form fields
driver.get("https://www.roboform.com/filling-test-all-fields")

