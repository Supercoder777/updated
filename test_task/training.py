from selenium import webdriver
from selenium.webdriver.firefox.service import Service

service_obj = Service("/Applications/geckodriver");
driver = webdriver.Firefox(service=service_obj)
driver.get("https://hub.knime.com")