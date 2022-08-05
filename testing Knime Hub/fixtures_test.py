import pytest
from selenium import webdriver


@pytest.fixtures()
def init_web_driver():
   print("\n in web driver init")
   webdriver.chrome()
   return webdriver.chrome()

@pytest.fixture()
   def second_fixture():

def test_my_first_driver(init_web_driver):

   driver = init_web_driver

   driver.get("http://hub.knime.com")

   print("\n how do i fix this mess")




