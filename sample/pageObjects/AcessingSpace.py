from selenium.webdriver.common.by import By

from pageObjects.Createspace import CreateSpace


class AccessingSpace:

    def __int__(self, driver):
        self.driver = driver

    space = (By.CSS_SELECTOR, ".avatar.avatar-placeholder")

    def Space(self):
        self.driver.find_element(*AccessingSpace.space).click()
        createSpace = CreateSpace(self.driver)
        return
