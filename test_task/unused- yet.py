# driver.find_element_by_link_text("Create account").click()

# driver.find_element(By.ID, "edit-name").send_keys("dami")

# driver.find_element(By.CSS_SELECTOR, '.myelement child').text

# driver.find_element(By.CSS_SELECTOR, '.#edit-name').send_keys("damilola.samuel94@gmail.com")

# driver.find_element(By.CSS_SELECTOR, '.#edit-pass').send_keys("zAddi623_")

# driver.find_element(By.CSS_SELECTOR, '.button.primary.compact').click()

# driver.find_element(By.CSS_SELECTOR, '.accept-button.button.primary').click()

# driver.find_element(By.CSS_SELECTOR, "//span[normalize-space()='Spaces']").click()

# driver.find_element(By.XPATH, "//nav[@class='sidemenu']//span[contains(text(),'spaces'").click()

# driver = webdriver.Chrome(executable_path="/Applications/Utilities/chromedriver")

# wait = WebDriverWait(driver, 4)
# wait.until(expected_conditions.presence_of_element_located(By.CSS_SELECTOR,".message"))

# driver.find_element(By.CSS_SELECTOR,".message").text

# alert = driver.
# alertText = alert.text
# print(alertText)
# driver.find_element(By.CLASS_NAME, "Successfully")
# assert "Success" in alertText

# driver.get_screenshot_as_file("created space.png")

# driver.close()



# driver.find_element(By.XPATH, "//button[normalize-space()='Delete space']").click()

#


import os

i = 0
while os.path.exists("sample%s.xml" % i):
    i +=1

    fh = open("sample%s.xml" % i, "w")
    fh.close()