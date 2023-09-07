import time
from utils.selActionOnWebElements import ElementActions as EA
import allure
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.locators import loc_loginpage
from page_objects.locators import loc_dashboardpage as db
from page_objects.locators import loc_common as cm
from testdata.labels_messages import labels

class LoginPage():
    def __init__(self, driver, wait, logger):
        self.driver = driver
        self.wait = wait
        self.logger = logger

    @allure.step("Enter username")
    def setUsername(self, username:str):
        self.logger.info("=== Inside method setUsername ===")
        username_txtbox = EA.find_Element(By.NAME,loc_loginpage.loc_input_usernametxtbox, self.driver)
        EA.input_text(username_txtbox,username, self.driver, self.logger)
        self.logger.info("=== Method setUsername Ends ===")

    @allure.step("Enter password")
    def setPassword(self, password:str):
        self.logger.info("====== Inside setPassword Method ======")
        password_txtbox = EA.find_Element(By.NAME,loc_loginpage.loc_input_passwordtxtbox,  self.driver)
        EA.input_text(password_txtbox,password, self.driver, self.logger)
        self.logger.info("=========== setPassword Executed successfully =======")

    @allure.step("Click on login button")
    def clickOnLogin(self):
        btn_login = self.driver.find_element(By.XPATH, loc_loginpage.loc_button_login)
        EA.click_button(btn_login, self.driver)

    @allure.story("Valid Login story")
    def verify_ValidLogin(self):
        self.wait.until(EC.url_contains("/dashboard/index"))
        label_myActions = self.driver.find_element(By.XPATH,db.loc_myactions_label)
        assert label_myActions.is_displayed()==True
        assert label_myActions.text == labels.label_db_myactions

        img_profile = self.driver.find_element(By.XPATH,cm.loc_img_profpic)
        assert img_profile.is_displayed()==True

        profile_username = self.driver.find_element(By.XPATH,cm.loc_p_username)
        assert profile_username.is_displayed() == True
#        assert profile_username.text == labels.label_cm_profile_username

        db_menu = self.driver.find_element(By.XPATH,cm.loc_h_menutitle)
        assert db_menu.is_displayed() == True
        assert db_menu.text == labels.label_db_dashboard_menu