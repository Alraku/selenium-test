from time import sleep
import logging

import utils.globals as globals
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

LOGGER = logging.getLogger(__name__)

class PageHome:

    id_search_field = 'headerSearch'
    id_location_field = 'cityField'
    id_location_suggestion = 'autosuggest-geo-ul'
    submit_search_button = 'submit-searchmain'
    add_advert_button = 'postNewAdLink'


    def __init__(self, driver):
        self.driver = driver  

    
    def search_phrase(self, search_term: str, timeout: int = 3, location: str = ''):
        search_element = self.driver.find_element(By.ID, self.id_search_field)
        location_element = self.driver.find_element(By.ID, self.id_location_field)
        search_element.send_keys(search_term)
        location_element.send_keys(location)

        try:
            element = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.ID, self.id_location_suggestion)))
            list_items = element.find_elements(By.TAG_NAME, "li")
            list_items[0].click()
        except TimeoutException as Exception:
            print("Element Not Found")
            raise Exception

        location_element.submit()
        sleep(timeout)


    def click_add_advert_button(self):
        #self.driver.find_element(By.ID, self.add_advert_button).click()
        self.driver.get(globals.base_url + '/nowe-ogloszenie')
        try:
            element = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((
                    By.CLASS_NAME, "css-spwpto")))
            element.click()
        except TimeoutException as Exception:
            print("Element not found in desired time")
            raise Exception