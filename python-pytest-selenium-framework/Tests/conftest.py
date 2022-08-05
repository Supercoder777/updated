import service as service
import pytest
import driver as driver
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
from urllib3 import request


@pytest.fixture(scope="class")
def invoke_browser():
    service_obj = service("/Users/HP/Downloads/chromedriver")
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(5)
    driver.get("https://hub.knime.com/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()
