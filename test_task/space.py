import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="/Applications/Utilities/chromedriver")

driver.get("https://hub.knime.com/damilola001/spaces")

driver.implicitly_wait(5)

driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, ".accept-button.button.primary").click()

driver.find_element(By.XPATH, "//nav[@class='sidemenu']//span[contains(text(),'spaces'").click()

driver.find_element(By.XPATH,"//button[normalize-space()='Private space']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='Public space']").click()

driver.find_element(By.TAG_NAME, "textarea").send_keys("Space_created")


driver.find_element(By.XPATH,"//button[@class='toggle function-button single active']//*[name()='svg']").click()

driver.find_element(By.XPATH,"//button[normalize-space()='Delete space']").click()

#driver.find_element(By.XPATH,"//button[@title='Save']//*[name()='svg']").click()

#driver.find_element(By.XPATH,"//button[@title='Save']//*[name()='svg']").click()

#driver.find_element(By.XPATH,"//button[@title='Save']//*[name()='svg']").click()