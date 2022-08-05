import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager import driver

from utilities.BaseClass import BaseClass
from pageObjects.SignInPage import SignInPage


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        access = SignInPage(self, driver)
        access.hubAccess().click()
        signInPage = SignInPage.s
        signInPage.

        self.driver.find_element(By.CSS_SELECTOR, '.accept-button.button.primary').click()
        self.driver.find_element(By.XPATH, " //button[normalize-space()='Sign in']").click()
        self.driver.find_element(By.CSS_SELECTOR, " #edit-name").send_keys("samuel4luve@yahoo.com")
        self.driver.find_element(By.CSS_SELECTOR, "#edit-pass").send_keys("zAddi623_")
        self.driver.find_element(By.CSS_SELECTOR, "#edit-submit").click()
        self.driver.find_element(By.CSS_SELECTOR, ".avatar.avatar-placeholder").click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[normalize-space()='Spaces']"))).click()
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Private space']").click()
        # driver.find_element(By.XPATH, "//button[normalize-space()='Public space']").click()
        self.driver.find_element(By.TAG_NAME, "textarea").send_keys("Space_created005")
        self.driver.find_element(By.XPATH, "//button[@title='Save']//*[name()='svg']").click()
        successmsg = self.driver.find_element(By.CSS_SELECTOR, ".message").text
        print(successmsg)
        self.driver.get_screenshot_as_file("created space.png")
        assert "successfully" in successmsg
