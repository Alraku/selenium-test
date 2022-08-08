from pages._base import BasePage
from pages._locators import PageResultsLocators as Locator
from selenium.webdriver.common.by import By


class PageResults(BasePage):

    def check_if_element_reloaded(self):
        results_skeleton_wrapper = self.find_element(Locator.RESULTS_SKELETON_WRAPPER)
        self.wait(3)
        return results_skeleton_wrapper
            

    def extract_number_from_str(self):
        return int(
            "".join(filter(
                str.isdigit,
                self.find_element(Locator.NUMBER_OF_ADS_FOUND)).text))


    def click_checkbox(self, checkbox_name):
        self.driver.find_element(By.ID, checkbox_name).click()
        self.find_element(Locator.CHECKBOX_NAME)