import pytest
import selenium
import collections
from selenium.webdriver.chrome.webdriver import WebDriver


def init_web_driver():

    print("\n open the web driver")

    driver: WebDriver = WebDriver.chrome()

    yield driver

    print("this is after the yield")

    driver.close()

def test_website_with_driver():

    driver: WebDriver = init_web_driver()

    driver.get("http://facebook.com")

    print("\n hope second test works")