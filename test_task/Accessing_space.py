
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions, select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


# service_obj = Service("/Users/HP/Downloads/chromedriver-2")
# driver = webdriver.Chrome(service=service_obj)
# driver = webdriver.Chrome(ChromeDriverManager().install)

service_obj = Service("/Users/HP/Downloads/chromedriver")
driver = webdriver.Chrome(service=service_obj)

# driver = webdriver.Chrome(executable_path="/Users/HP/Downloads/chromedriver-2")
driver.implicitly_wait(5)
driver.get("https://hub.knime.com/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, '.accept-button.button.primary').click()
driver.find_element(By.XPATH, " //button[normalize-space()='Sign in']").click()
driver.find_element(By.CSS_SELECTOR, " #edit-name").send_keys("samuel4luve@yahoo.com")
driver.find_element(By.CSS_SELECTOR, "#edit-pass").send_keys("zAddi623_")
driver.find_element(By.CSS_SELECTOR, "#edit-submit").click()
driver.find_element(By.CSS_SELECTOR, ".avatar.avatar-placeholder").click()
#wait = WebDriverWait(driver, 5)
#wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "//span[normalize-space()='Spaces']").click()))
#driver.find_element(By.XPATH, "//span[normalize-space()='Spaces']").click()
#driver.find_element(By.XPATH, "//nav[@class='sidemenu']//span[contains(text(),'spaces'").click()
#driver.find_element(By.XPATH,"//button[normalize-space()='Private space']").click()
#driver.find_element(By.XPATH,"//button[normalize-space()='Public space']").click()
#driver.find_element(By.TAG_NAME, "textarea").send_keys("Space_created")
#driver.find_element(By.XPATH,"//button[@class='toggle function-button single active']//*[name()='svg']").click()
#driver.find_element(By.XPATH,"//button[normalize-space()='Delete space']").click()
# select
