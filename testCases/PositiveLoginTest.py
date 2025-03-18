import time

import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test__001__login:
    baseURL = ReadConfig.getBaseURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_verify_new_pageURL(self, setup):
        self.logger.info("************ Test__001__login **************")
        self.logger.info("************ Browser started... **************")
        self.logger.info("************ Verifying new page Url Test **************")
        driver = setup
        driver.get(self.baseURL)
        driver.maximize_window()
        lp = LoginPage(driver)
        lp.input_username(self.username)
        lp.input_password(self.password)
        lp.click_submit_button()
        if lp.check_url():
            assert True
            driver.close()
            self.logger.info("************ Verify new page Url Test is passed **************")
        else:
            driver.save_screenshot(".\\Screenshots\\"+"test_test_verify_new_pageURL.png")
            driver.close()
            self.logger.error("************ Verify new page Url Test is failed **************")
            assert False

    @pytest.mark.regression
    def test_page_expected_text(self, setup):
        self.logger.info("************ verifying page text Test **************")
        driver = setup
        driver.get(self.baseURL)
        driver.maximize_window()
        lp = LoginPage(driver)
        lp.input_username(self.username)
        lp.input_password(self.password)
        lp.click_submit_button()
        if lp.check_page_text():
            assert True
            driver.close()
            self.logger.info("************ Expected page text Test is passed **************")
        else:
            driver.save_screenshot(".\\Screenshots\\" + "test_page_expected_text.png")
            driver.close()
            self.logger.error("************ Expected page text Test is failed **************")
            assert False

    @pytest.mark.regression
    def test_button_is_displayed(self, setup):
        self.logger.info("************ verifying displayed logout button **************")
        driver = setup
        driver.get(self.baseURL)
        driver.maximize_window()
        lp = LoginPage(driver)
        lp.input_username(self.username)
        lp.input_password(self.password)
        lp.click_submit_button()
        if lp.check_logout_button():
            assert True
            driver.close()
            self.logger.info("************ logout displayed test ist passed  **************")
        else:
            driver.save_screenshot(".\\Screenshots\\" + "test_button_is_displayed.png")
            driver.close()
            self.logger.error("************ logout displayed test ist failed  **************")
            assert False
            #driver.close()
