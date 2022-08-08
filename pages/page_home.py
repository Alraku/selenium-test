import utils.globals as globals
from pages._base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages._locators import PageHomeLocators as Locator


class PageHome(BasePage):

    def __init__(self, driver) -> None:
        super().__init__(driver, '')  

    
    def search_phrase(self, search_term: str, location: str = '') -> None:
        self.logger.info("Entering search term and location into the input fields.")
        search_box = (self.find_element(Locator.SEARCH_BOX)
            .send_keys(search_term))

        location_box = (self.find_element(Locator.INPUT_LOCATION)
            .send_keys(location))

        # Mozliwe ze będzie potrzebna funkcja dla "element_to_be_clicable".
        location_suggestion = self.find_element(Locator.INPUT_LOCATION_SUGGESTION)
        location_list = location_suggestion.find_elements(By.TAG_NAME, "li")
        location_list[0].click()
  
        location_box.submit()
        self.wait(3)


    def click_add_advert_button(self) -> None:
        #self.driver.find_element(By.ID, self.add_advert_button).click()
        # Mozliwe ze będzie potrzebna funkcja dla "element_to_be_clicable".
        # TODO Nalezy zmienic na rzeczywiste klikanie buttonu, nie zmiana adresu
        self.driver.get(globals.BASE_URL + '/nowe-ogloszenie')
        BUTTON_ADD_ADVERT = (By.CLASS_NAME, "ss-spwpto")
        
        add_advert_button = (self.find_element(BUTTON_ADD_ADVERT)
            .click())