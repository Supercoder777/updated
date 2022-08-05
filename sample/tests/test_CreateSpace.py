from utilities.BaseClass import BaseClass


class CreateSpace(BaseClass):

    def test_spaceCreation(self, getData):
        log = self.getlogger()
        createspace = CreateSpace(self.driver)
        log.info()
        createspace.getPrivateSpace().click()
        createspace.getPublicSpace().click()
        createspace.getName().send_keys(getData["nameOfSpace"])
        createspace.getSaveName().click()

        successMsg = createspace.getSuccessMsg().text
        print(successMsg)

        assert ("successfully" in successMsg)