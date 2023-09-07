import time

import allure
import pytest
from utils.logging import GetLog
from utils import excelFileOperations as Exl
from page_objects.business_logic.BL_LoginPage import LoginPage
from utils.readConfigFile import ConfigFileOperations

@allure.epic("Login functionality")
@pytest.mark.usefixtures("setup&teardown")
class Test_LoginPage():

    @allure.testcase("https://docs.qameta.io/allure/","Valid data test")
    @allure.description("This testcase verifies user should be logged in successfully")
    @allure.feature("Login with valid data")
    def test_LoginWithValidCredentials(self):

        self.logger.critical("============ testcase test_LoginWithValidCredentials start ==========")
        lp = LoginPage(self.driver, self.wait, self.logger)
        lp.setUsername("Admin")
        lp.setPassword("admin123")
        lp.clickOnLogin()
        # lp.verify_ValidLogin()
        # time.sleep(10)
        # self.logger.info("===+++++ " + ConfigFileOperations.getValueFromConfig("C:\\Workspace\\Python_Workspace\\com.orangehrmlive.management.hr.ui_automation_selframework\\config_files\\config.ini","login_user_details","username")+ " ===+++++")
        # self.logger.warning("====== testcase executed successfully ==========")
        # self.logger.error("++++++++++++++++++++++++++++++++++++++++++++++")