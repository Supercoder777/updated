from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/HP/Downloads/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.knime.com/user/login?destination=/oauth2/authorize/")

service_obj = Service("/Users/HP/Downloads/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.knime.com/user/login?destination=/oauth2/authorize/")
