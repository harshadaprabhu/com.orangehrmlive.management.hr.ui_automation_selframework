import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from testdata.labels_messages import labels


class ElementActions():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, timeout=5)
    ele = driver.find_element()
    select = Select(ele)

    @staticmethod
    def find_Element(locType:By, locValue:str, driver):
        return driver.find_element(locType, locValue)

    @staticmethod
    def find_Elements(*loc):
        return ElementActions.driver.find_elements(*loc)

    @staticmethod
    def input_text(element:webelement, text, driver, logger):
        ElementActions.wait.until(EC.element_to_be_clickable(element))
        element.clear()
        element.send_keys(text)
        if element.get_attribute("value")==text:
             assert True
        else:
            driver.save_screenshot(".\\screenshots\\" + text + ".png")
            logger.error(text + " doesnot match with " + element.get_attribute("value"))
            assert False

    @staticmethod
    def verifyText_click(element:webelement,driver, text:str):
        ElementActions.wait.until(EC.element_to_be_clickable(element))
        btn_text = element.text
        if btn_text == text:
            element.click()
        else:
            allure.attach(driver.get_screenshot_as_png(),name=btn_text,attachment_type=AttachmentType.PNG)
            assert False

    @staticmethod
    def click(element:webelement,driver):
        ElementActions.wait.until(EC.element_to_be_clickable(element))
        element.click()

    @staticmethod
    def verifyTooltip_click(element:webelement,driver, tooltip:str, attributeName:str):
        ElementActions.wait.until(EC.element_to_be_clickable(element))
        ele_tooltip = element.get_attribute(attributeName)
        if ele_tooltip == tooltip:
            element.click()
        else:
            allure.attach(driver.get_screenshot_as_png(),name=ele_tooltip,attachment_type=AttachmentType.PNG)
            assert False

    @staticmethod
    def isElementDisabled(element:webelement, logger, driver):
        if element.is_displayed() == True and element.is_enabled() == False:
            assert True
            logger.info(element + " is disabled")
        else:
            logger.info(element + " is enabled")
            allure.attach(driver.get_screenshot_as_png(), name="Element is enabled", attachment_type=AttachmentType.PNG)
            assert False

    @staticmethod
    def isSelected(element:webelement, logger, driver, visibleText:str):
        status = None
        ElementActions.wait.until(EC.element_to_be_clickable(element))
        if element.text == visibleText and element.is_selected()==True:
            assert True
            status = True
            logger.info(element + " is selected")
        else:
            logger.info(element + " is not selected")
            allure.attach(driver.get_screenshot_as_png(), name="Element is not selected",
                          attachment_type=AttachmentType.PNG)
            status = False

        return status

    @staticmethod
    def selectCheckboxRadioBtn(element:webelement, logger, driver, visibleText):
        if ElementActions.isSelected(element, logger, driver, visibleText) == True:
            pass
            logger.info("Checkbox is already selected")
        elif ElementActions.isSelected(element, logger, driver, visibleText) == False:
            if element.text == visibleText:
                ElementActions.click(element, driver)
                assert True
                logger.info(element + " is selected")
            else:
                logger.info(element + " is not selected")
                assert False

    @staticmethod
    def deselectCheckbox(element:webelement, logger, driver, visibleText):
        if ElementActions.isSelected(element, logger, driver, visibleText) == True:
            if element.text == visibleText:
                ElementActions.click(element, driver)
                assert True
                logger.info(element + " is now deselected")
            else:
                logger.info(element + " is not deselected")
                assert False
        elif ElementActions.isSelected(element, logger, driver, visibleText) == False:
            logger.info(element + " is not selected")

    @staticmethod
    def selectFromDropDownUsingText(element:webelement, logger, visibleText:str):
        ElementActions.wait.until(EC.element_to_be_clickable(element))
        select = Select(element)
        selectedOption = select.first_selected_option
        if selectedOption.text == visibleText:
            logger.info(selectedOption + " is already selected")
            pass
        elif selectedOption.text != visibleText:
            select.select_by_visible_text(visibleText)
            selectedOption = select.first_selected_option
            assert selectedOption.text == visibleText
            logger.info(selectedOption + " is now selected")

    @staticmethod
    def selectFromDropDownUsingIndex(element:webelement, logger, visibleText:str, index:int):
        ElementActions.wait.until(EC.element_to_be_clickable(element))
        select = Select(element)
        selectedOption = select.first_selected_option
        if selectedOption.text == visibleText:
            logger.info(selectedOption + " is already selected")
            pass
        elif selectedOption.text != visibleText:
            select.select_by_index(index)
            selectedOption = select.first_selected_option
            assert selectedOption.text == visibleText
            logger.info(selectedOption + " is now selected")

    @staticmethod
    def selectFromDropDownUsingValue(element:webelement, logger, visibleText:str, value:str):
        ElementActions.wait.until(EC.element_to_be_clickable(element))
        select = Select(element)
        selectedOption = select.first_selected_option
        if selectedOption.text == visibleText:
            logger.info(selectedOption + " is already selected")
            pass
        elif selectedOption.text != visibleText:
            select.select_by_value(value)
            selectedOption = select.first_selected_option
            assert selectedOption.text == visibleText
            logger.info(selectedOption + " is now selected")

    @staticmethod
    def selectMultipleOptionsFromDropDownUsingValue(element: webelement, logger, visibleText: str, value: str):
        ElementActions.wait.until(EC.element_to_be_clickable(element))
        select = Select(element)
        selectedOptions = select.all_selected_options
        for selectedOption in selectedOptions:
            if selectedOption.text == visibleText:
                logger.info(selectedOption + " is already selected")
                pass
            elif selectedOption.text != visibleText:
                select.select_by_value(value)
                selectedOption = select.first_selected_option
                assert selectedOption.text == visibleText
                logger.info(selectedOption + " is now selected")

    @staticmethod
    def selectMultipleOptionsFromDropDownUsingText(element: webelement, logger, visibleText: str):
        ElementActions.wait.until(EC.element_to_be_clickable(element))
        select = Select(element)
        selectedOptions = select.all_selected_options
        for selectedOption in selectedOptions:
            if selectedOption.text == visibleText:
                logger.info(selectedOption + " is already selected")
                pass
            elif selectedOption.text != visibleText:
                select.select_by_visible_text(visibleText)
                selectedOption = select.first_selected_option
                assert selectedOption.text == visibleText
                logger.info(selectedOption + " is now selected")


    @staticmethod
    def selectMultipleOptionsFromDropDownUsingIndex(element: webelement, logger, visibleText: str, index:int):
        ElementActions.wait.until(EC.element_to_be_clickable(element))
        select = Select(element)
        selectedOptions = select.all_selected_options
        for selectedOption in selectedOptions:
            if selectedOption.text == visibleText:
                logger.info(selectedOption + " is already selected")
                pass
            elif selectedOption.text != visibleText:
                select.select_by_index(index)
                selectedOption = select.first_selected_option
                assert selectedOption.text == visibleText
                logger.info(selectedOption + " is now selected")

    @staticmethod
    def selectMultipleOptionsFromDropDownUsingIndex(element: webelement, logger, visibleText: str, index:int):
        ElementActions.wait.until(EC.element_to_be_clickable(element))
        select = Select(element)
        selectedOptions = select.all_selected_options
        for selectedOption in selectedOptions:
            if selectedOption.text == visibleText:
                select.deselect_by_index(index)
                logger.info(selectedOption + " is now deselected")
            elif selectedOption.text != visibleText:
                logger.info(selectedOption + " is already deselected")





