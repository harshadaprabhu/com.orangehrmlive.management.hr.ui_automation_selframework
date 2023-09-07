from selenium import webdriver
from selenium.common import NoSuchFrameException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class frame():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, timeout=5)
    h = driver.window_handles
    driver.switch_to.window()


    @staticmethod
    def switch_to_frame(driver, wait, by:any, value:str):
        frame = wait.until(EC.presence_of_element_located((by, value)))
        driver.switch_to.frame(frame)

    @staticmethod
    def switch_to_frame_using_wait(wait,logger, by:any, value:str):
        try:
            if wait.until(EC.frame_to_be_available_and_switch_to_it((by, value)))==True:
                logger.info("User is switched to the frame")
                assert True
            else:
                assert False
        except NoSuchFrameException:
                logger.error("Either frame does not exists")
        except AssertionError:
                logger.error("Assertion failed since focus is not switched to the frame")

    @staticmethod
    def switch_to_default_content(driver):
       driver.switch_to.default_content()

    @staticmethod
    def switch_to_parent(driver):
        driver.switch_to.parent_frame()

class alert():
    @staticmethod
    def verify_text_and_accept_alert(alerttext:str, wait):
        alert = wait.until(EC.alert_is_present())
        if alert.text == alerttext:
            alert.alert.accept()
        else:
            alert.dismiss()

    @staticmethod
    def dismiss_alert(wait):
        alert = wait.until(EC.alert_is_present())
        alert.dismiss()

    @staticmethod
    def entertext_in_alert_accept(wait, inputtext):
        alert = wait.until(EC.alert_is_present())
        alert.send_keys(inputtext)
        alert.accept()

class windowhandle():
    @staticmethod
    def get_window_handles(driver, wait, logger):
        try:
            if wait.until(EC.new_window_is_opened()) == True:
                handles = driver.window_handles
                return handles
            else:
                assert False
        except  Exception:
            logger.error("New windows are not opened")

    @staticmethod
    def get_current_window_handle(driver, wait, logger):
        if wait.until(EC.new_window_is_opened()) == True:
            handle = driver.current_window_handle
            return handle

    @staticmethod
    def switch_to_window(windowname:str, driver, wait, logger):
        handles = windowhandle.get_window_handles(driver, wait, logger)
        if handles.count() > 0:
            driver.switch_to.window(windowname)

    @staticmethod
    def switch_to_window(windowname:str, driver, wait, logger):
        handle = windowhandle.get_current_window_handle(driver, wait, logger)
        if handle.count() == 1:
            driver.switch_to.new_window()



