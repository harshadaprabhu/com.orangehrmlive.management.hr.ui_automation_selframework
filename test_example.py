import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(5)

wait = WebDriverWait(driver, timeout=10)
loc_button_login = "//div[@class='oxd-form-actions orangehrm-login-action']/button"
wait.until(EC.visibility_of_element_located((By.XPATH,loc_button_login)))
time.sleep(5)
print("test successful")


