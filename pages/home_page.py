from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class PageHome():

    id_search_field = 'headerSearch'
    id_location_field = 'cityField'
    id_location_suggestion = 'autosuggest-geo-ul'
    submit_search_button = 'submit-searchmain'


    def __init__(self, driver):
        self.driver = driver  

    
    def search_phrase(self, search_term: str, timeout: int = 3, location: str = ''):
        search_element = self.driver.find_element(By.ID, self.id_search_field)
        location_element = self.driver.find_element(By.ID, self.id_location_field)
        search_element.send_keys(search_term)
        location_element.send_keys(location)

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, self.id_location_suggestion)))
            list_items = element.find_elements(By.TAG_NAME, "li")
            list_items[0].click()
        except NoSuchElementException:
            print("Element Not Found")

        location_element.submit()
        sleep(timeout)