from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Applications/Utilities/chromedriver")

driver.get("https://hub.knime.com/")

driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, '.accept-button.button.primary').click()

driver.find_element(By.CSS_SELECTOR, '.button.primary.compact').click()







#driver.find_element_by_css_selector("#edit-name").send_keys("samuel4luve@yahoo.com")

#driver.find_element_by_css_selector("//button[contains(text(),'Accept and close')]").click()

#driver.find_element_by_class_name("")

#driver.find_element_by_xpath("//button[contains(text(),'Sign in')]").click()

#driver.find_element('CSS_SELECTOR'.'button.primary.compact')

driver.find_element_by_css_selector("#edit-submit").click()

driver.close()

driver.find_element('css selector', '.myelement child').text
#for addding wait time in the code to allow to load
driver.implicitly_wait(4)

#to switch to a new window when you click and a new window opens
#to get window name
print = driver.window_handles
#windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[#number of window needed])




driver.find_element(By.ID, "").send_keys("")
driver.find_element(By.ID, "").send_keys("")

#Work with JavaScript in selenium automation

#to Scroll in JavaScript
#console -  type in #Window.scrollby()
#can also use Window.scrollby(0, document.body.scrollHeight)


#To use with python
driver.execute_script(#"JAvaScript code")

#Screenshot with Python
driver.get_screenshot_as_file(#name of file)

#Run test in headless mode(without seeing the browser)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/HP/Downloads/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.get("https://www.knime.com/user/login?destination=/oauth2/authorize/")


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")



from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Applications/Utilities/chromedriver")

driver.get("https://hub.knime.com/")

driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, '.accept-button.button.primary').click()

driver.find_element(By.CSS_SELECTOR, '.button.primary.compact').click()

#Sorting tables
#steps

#click the top of the column


#collect list of items (browserSortedItemList) (List)



#Sort the collected Items



#BrowserSortedItems = NewSortedItems


#ChromeOptionsDemo

#should be written before chrome is invoked

chrome_options = webdriver.ChromeOptions
chrome_options.add_argument("--start-maximized")

#private conections(SSL certificate)

chrome_options.add_argument("--ignore-certificate-errors")

service_obj = Service("/Users/HP/Downloads/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.get("https://www.knime.com/user/login?destination=/oauth2/authorize/")

