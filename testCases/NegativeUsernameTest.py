from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage

class Test__002__login:
    baseURL = ReadConfig.getBaseURL()
    incorrectUsername = ReadConfig.get_incorrectUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_incorrect_username(self, setup):
        self.logger.info("*************Test__002__login**************")
        self.logger.info("*************Browser is opened**************")
        self.logger.info("*************Test with incorrect Username is performed**************")
        driver = setup
        driver.get(self.baseURL)
        driver.maximize_window()
        lp = LoginPage(driver)
        lp.input_username(self.incorrectUsername)
        lp.input_password(self.password)
        lp.click_submit_button()
        if lp.check_incorrectUsername_text():
            assert True
            driver.close()
            self.logger.info("*************Incorrect Username Test is passed**************")

        else:
            driver.close()
            self.logger.error("*************Incorrect Username Test is failed**************")
            self.logger.error("*************error message wasn't displayed**************")
            assert False


    def test_username_errorMessage(self, setup):
        self.logger.info("*************Browser is opened**************")
        self.logger.info("*************Test username error message is performed**************")
        driver = setup
        driver.get(self.baseURL)
        driver.maximize_window()
        lp = LoginPage(driver)
        lp.input_username(self.incorrectUsername)
        lp.input_password(self.password)
        lp.click_submit_button()
        if lp.check_username_errorMessage():
            assert True
            driver.close()
            self.logger.info("*************Username error message Test is passed**************")
        else:
            driver.close()
            self.logger.info("*************Username error message Test is failed**************")
            assert False



