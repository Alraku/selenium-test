import time

from framework.wrappers import find_element
from pages._locators import SearchResultsPageLocators as Locator

from selenium.webdriver.common.by import By


class PageSearchResults:

    def __init__(self, driver):
        self.driver = driver


    def check_if_element_reloaded(self):
        results_skeleton_wrapper = find_element(
            self.driver,
            Locator.RESULTS_SKELETON_WRAPPER)
        time.sleep(3)
        return results_skeleton_wrapper
            

    def extract_number_from_str(self):
        return int(
            "".join(filter(
                str.isdigit,
                find_element(self.driver, Locator.NUMBER_OF_ADS_FOUND)).text))


    def click_checkbox(self, checkbox_name):
        self.driver.find_element(By.ID, checkbox_name).click()
        find_element(self.driver, Locator.CHECKBOX_NAME)