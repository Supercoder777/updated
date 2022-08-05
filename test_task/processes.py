from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("/Users/HP/Downloads/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://hub.knime.com/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, '.accept-button.button.primary').click()
driver.find_element(By.XPATH, " //button[normalize-space()='Sign in']").click()
driver.find_element(By.CSS_SELECTOR, " #edit-name").send_keys("samuel4luve@yahoo.com")
driver.find_element(By.CSS_SELECTOR, "#edit-pass").send_keys("zAddi623_")
driver.find_element(By.CSS_SELECTOR, "#edit-submit").click()
verifyLog = driver.title
print(verifyLog)
driver.get_screenshot_as_file("dami hub.png")
assert "KNIME Hub" in verifyLog
driver.find_element(By.CSS_SELECTOR, ".avatar.avatar-placeholder").click()
wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[normalize-space()='Spaces']"))).click()
driver.find_element(By.XPATH, "//button[normalize-space()='Private space']").click()
# driver.find_element(By.XPATH, "//button[normalize-space()='Public space']").click()
driver.find_element(By.TAG_NAME, "textarea").send_keys("Space_created0051")
driver.find_element(By.XPATH, "//button[@title='Save']//*[name()='svg']").click()
successMsg = driver.find_element(By.CSS_SELECTOR, ".message").text
print(successMsg)
driver.get_screenshot_as_file("created space.png")
assert "successfully" in successMsg
driver.close()
