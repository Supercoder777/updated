from selenium.webdriver.common.by import By


class CreateSpace:

    def __int__(self, driver):
        self.driver = driver

    privateSpace = (By.XPATH, "//button[normalize-space()='Private space']")
    PublicSpace = (By.XPATH, "//button[normalize-space()='Public space']")
    name = (By.TAG_NAME, "textarea")
    saveName = (By.XPATH, "//button[@title='Save']//*[name()='svg']")
    successMsg = (By.CSS_SELECTOR, ".message")

    def getPrivateSpace(self):
        return self.driver.find_element(*CreateSpace.privateSpace)

    def getPublicSpace(self):
        return self.driver.find_element(*CreateSpace.PublicSpace)

    def getName(self):
        return self.driver.find_element(*CreateSpace.name)

    def getSaveName(self):
        return self.driver.find_element(*CreateSpace.saveName)

    def getSuccessMsg(self):
        return self.driver.find_element(*CreateSpace.successMsg)




