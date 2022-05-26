import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class PageSearchResults:

    number_of_ads_found = "div[data-testid='total-count']"
    results_skeleton_wrapper = "ul[data-testid='qa-skeleton-wrapper']"

    def __init__(self, driver):
        self.driver = driver


    def check_if_element_reloaded(self):
        try:
            element_present = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.results_skeleton_wrapper)))
            time.sleep(3)
            return element_present

        except TimeoutException as Exception:
            print("Element could not be found")
            raise Exception
            

    def extract_number_from_str(self):
        return int("".join(filter(str.isdigit, self.driver.find_element(By.CSS_SELECTOR, self.number_of_ads_found).text)))


    def click_checkbox(self, checkbox_name):
        self.driver.find_element(By.ID, checkbox_name).click()