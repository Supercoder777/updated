from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/HP/Downloads/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.knime.com/user/login?destination=/oauth2/authorize/")
driver.find_element(By.LINK_TEXT, "Create account").click()
driver.find_element(By.CSS_SELECTOR, "#edit-mail").send_keys("samuel4luve@yahoo.com")
driver.find_element(By.CSS_SELECTOR, "#edit-name").send_keys("damilola01987")
driver.find_element(By.CSS_SELECTOR, "#edit-field-firstname-0-value").send_keys("wayne")
driver.find_element(By.CSS_SELECTOR, "#edit-field-lastname-0-value").send_keys("batman")
driver.find_element(By.CSS_SELECTOR, "#edit-field-company-0-value").send_keys("mailer")
driver.find_element(By.XPATH, "//input[@id='edit-field-receive-updates-value']").click()
driver.find_element(By.CSS_SELECTOR, "#edit-legal-accept").click()
