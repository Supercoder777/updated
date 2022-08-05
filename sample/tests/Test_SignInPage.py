from pageObjects.SignInPage import SignInPage
from utilities.BaseClass import BaseClass
import pytest


class TestSignInPage(BaseClass):

    def test_fillForm(self, getdata):
        log = self.getlogger()
        log.info("email"+getdata["email"])
        signinpage = SignInPage(self.driver)
        signinpage.getEmail().send_keys(getdata["email"])
        signinpage.getPassword().send_keys(getdata["password"])
        signinpage.submit().click()

        verifyLog = self.driver.title().text

        print(verifyLog)

        self.driver.get_screenshot_as_file("dami hub.png")

        assert ("KNIME Hub" in verifyLog)

        @pytest.fixture(params=SignInPage.getTestData("test2"))
        def getData(self, request):
            return request.param