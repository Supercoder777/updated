import driver as driver
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import org.openqa.selenium.support.ui.select

#driver.wait(10)
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("/Users/HP/Downloads/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(5)

driver.get("https://hub.knime.com/")

driver.maximize_window()

print(driver.title)

print(driver.current_url)

driver.find_element(By.CSS_SELECTOR, ".accept-button.button.primary").click()
driver.find_element(By.XPATH, " //button[normalize-space()='Sign in']").click()
driver.find_element(By.CSS_SELECTOR, " #edit-name").send_keys("samuel4luve@yahoo.com")
driver.find_element(By.CSS_SELECTOR, "#edit-pass").send_keys("zAddi623_")
driver.find_element(By.CSS_SELECTOR, "#edit-submit").click()

wait = WebDriverWait(driver, 5)
wait.untill(expected_conditions.presence_of_element_located((By. )))

driver.find_element(By.XPATH,"//div[@class='submenu']//button[@type='button'" ).click()
driver.find_element(By.)




