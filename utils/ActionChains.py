from selenium.webdriver import ActionChains, Keys

from utils.selActionOnWebElements import ElementActions


class Action_Chain():
    @staticmethod
    def get_action_chain_object(driver):
        act = ActionChains(driver)
        act.scroll_to_element()
        return act

class MouseAction():
    @staticmethod
    def move_to_element(by, value, driver):
       element =  ElementActions.find_Element(by, value)
       act = Action_Chain.get_action_chain_object(driver)
       act.move_to_element(element).perform()

    @staticmethod
    def scroll(by, value, driver):
       element = ElementActions.find_Element(by, value)
       act = Action_Chain.get_action_chain_object(driver)
       act.scroll_to_element(element).perform()

class KeyActions():
    @staticmethod
    def send_keys(by, value, inputtext, driver):
        element = ElementActions.find_Element(by, value)
        act = Action_Chain.get_action_chain_object(driver)
        act.move_to_element(element).send_keys_to_element(element, inputtext).perform()

    @staticmethod
    def press_enter_key(driver):
        act = Action_Chain.get_action_chain_object(driver)
        act.send_keys(Keys.ENTER).perform()