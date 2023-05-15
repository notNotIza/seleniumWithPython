from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#chrome cannot be invoked directly
serviceObject = Service("")
webdriver.Chrome(service= serviceObject)