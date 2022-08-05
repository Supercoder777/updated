import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup(request):
    service_obj = Service("/Users/HP/Downloads/chromedriver")
    driver = webdriver.WebDriver(service=service_obj)
    driver.get("https://hub.knime.com/")
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()