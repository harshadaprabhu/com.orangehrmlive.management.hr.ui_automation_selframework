import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.locators import loc_loginpage
from utils.logging import GetLog

driver = None

@pytest.fixture(scope='class', name="setup&teardown")
def setup_teardown(request,browser):
    global driver
    logger = GetLog.getLogger()
    browser = 'chrome'
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        print("Invalid browser option")
    wait = WebDriverWait(driver, timeout=5)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(time_to_wait=5)
    wait.until(EC.visibility_of_element_located((By.XPATH, loc_loginpage.loc_button_login)))
    request.cls.driver = driver
    request.cls.wait = wait
    request.cls.logger = logger
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope='class')
def browser(request):
    return request.config.getoption("--browser")

def pytest_html_report_title(report):
    report.title = "My very own title!"




