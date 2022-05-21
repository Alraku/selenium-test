from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageHome():

    search_box = 'headerSearch'
    city_field = 'cityField'
    city_field_suggestion = 'search-choose-selected'
    submit_search_button = 'submit-searchmain'


    def __init__(self, driver):
        self.driver = driver  

    
    def search_phrase(self, phrase_to_search: str, timeout: int = 3, location: str = ''):
        self.driver.find_element(By.ID, self.search_box).send_keys(phrase_to_search)
        self.driver.find_element(By.ID, self.city_field).send_keys(location)

        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, self.city_field_suggestion))
            WebDriverWait(self.driver, 3).until(element_present)
        except:
            print("Element Not Found")

        self.driver.find_element(By.ID, self.submit_search_button).click()
        sleep(timeout)