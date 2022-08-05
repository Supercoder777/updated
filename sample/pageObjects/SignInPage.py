from selenium.webdriver.common.by import By

from pageObjects.AcessingSpace import AccessingSpace


class SignInPage:

    def __int__(self, driver):
        self.driver = driver
        hubaccess = (By.CSS_SELECTOR, '.accept-button.button.primary')
        signin = (By.XPATH, "//button[normalize-space()='Sign in']")
        username = (By.CSS_SELECTOR, " #edit-name")
        password = (By.CSS_SELECTOR, " #edit-pass")
        submit = (By.CSS_SELECTOR, "#edit-submit")
        verifylog = driver.title



    def signIn(self):
        self.driver.find_element(*SignInPage.signin)
        accessingSpace = AccessingSpace(self.driver)
        return accessingSpace

 #   def signInHub(self):
  #      self.driver.find_element(*SignInPage.hubaccess)
   #     access = SignInPage(self.driver)
   #     return access

    def userName(self):
        return self.driver.find_element(*SignInPage.username)

    def passWord(self):
        return self.driver.find_element(*SignInPage.password)

    def submit(self):
        return self.driver.find_element(*SignInPage.submit)
