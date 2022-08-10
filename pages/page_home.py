from pages._base import BasePage
from pages._locators import PageHomeLocators as Locator


class PageHome(BasePage):

    def __init__(self, driver) -> None:
        super().__init__(driver, '')

    def search_phrase(self, phrase: str, location: str = '') -> None:
        self.logger.info("Entering search term and location into the inputs.")
        self.find_element(Locator.SEARCH_BOX).send_keys(phrase)
        self.find_element(Locator.INPUT_LOCATION).send_keys(location)
        self.find_element(Locator.BUTTON_SUBMIT_SEARCH).click()
        self.wait(3)

    def click_add_advert(self) -> None:
        self.find_element(Locator.BUTTON_ADD_ADVERT).click()
        self.wait(3)
