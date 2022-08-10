import utils.globals as globals

from pages._base import BasePage
from pages._locators import PageAddAdvertLocators as Locator
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class PageAddAdvert(BasePage):

    def __init__(self, driver):
        super().__init__(driver, '/d/nowe-ogloszenie/')
        self._advert = None


    @property
    def advert(self):
        """Getter for advert property."""
        return self._advert


    @advert.setter
    def advert(self, advert):
        """Setter for advert property."""
        self._advert = advert


    def fill_in_fields(self):
        """Groups every small functions that fill formfiled on page."""
        self.fill_in_title()
        self.fill_in_suggested_category()
        self.fill_in_description()
        self.fill_in_additional_info()
        self.fill_in_contact_info()
        self.disable_delivery()


    def fill_in_title(self):
        """Waits for title form field to appear and fills a value in."""
        title = (self.find_element(Locator.INPUT_TITLE)
            .send_keys(self._advert.get('title')))


    def fill_in_suggested_category(self):
        """Opens category tray, waits for suggested category to appear and chooses it."""
        category_tray = (self.find_element(Locator.BUTTON_CATEGORY)
            .click())

        suggested_category = (self.find_element(Locator.BUTTON_SUGGESTED_CATEGORY)
            .click())


    def upload_photos(self):
        """Safari unsupported. Uploads photos from test data gallery."""
        for i in range(1, 4):
            photo_upload = self.find_element(Locator.INPUT_PHOTOS)
            photo_upload.send_keys(globals.ROOT_DIR + f"/data/gallery/{i}.jpg")


    def fill_in_description(self):
        """Searches for description form field and fills a value in."""
        self.page_scroll(850)
        description = (self.find_element(Locator.INPUT_DESCRIPTION)
            .send_keys(self._advert.get('description')))


    def fill_in_additional_info(self):
        """Searches for item condition dropdown list and chooses specific option."""
        self.check_price_value()
        self.check_advert_type()
        self.find_element(Locator.BUTTON_ITEM_CONDITION).click()

        try: 
            option = self._advert.get('item_condition')
            element = self.driver.find_element(
                By.XPATH, f"//*[@id='posting-form']/main/div[1]/div[4]/div/div[2]/ul/li[2]/div/div/ul/li[{option}]"
            )
            element.click()
        except NoSuchElementException as Exception:
            print("Element not found in desired time")
            raise Exception   


    def fill_in_contact_info(self):
        """Searches for contact location form field and fills a value in."""
        location = (self.find_element(Locator.INPUT_LOCATION)
            .clear()
            .send_keys(self._advert.get('location')))
            
        location = (self.find_element(Locator.suggested_location)
            .click())


    def preview_advert(self):
        """Redirects to new page containing pre-view of new advert."""
        pass


    def submit_advert(self):
        """Redirects to confirmation page and creates new advert."""
        (self.find_element(Locator.BUTTON_SUBMIT)
            .click())
        self.wait(3)


    def check_price_value(self):
        """
        Checks if string stored in price key is digit and if so fills form field.
        Otherwise selects for free or exchange options.
        """
        price = self._advert.get('price')
        if price.isdigit():
            element = (self.find_element(Locator.INPUT_PRICE)
                .send_keys(self._advert.get('price')))

        elif price == "free":
            element = (self.find_element(Locator.BUTTON_FREE)
                .click())

        elif price == "exchange":
            element = (self.find_element(Locator.BUTTON_EXCHANGE)
                .click())

    
    def check_advert_type(self):
        """
        Checks if string stored in advert type key is private or business.
        Selects proper type of advert.
        """
        type = self._advert.get('advert_type')
        if type == "private":
            element = (self.find_element(Locator.BUTTON_TYPE_PRIVATE)
                .click())

        elif type == "business":
            element = (self.find_element(Locator.BUTTON_TYPE_BUSINESS)
                .click())


    def disable_delivery(self):
        """Disables option for integrated delivery system."""
        self.page_scroll(1800)
        delivery = (self.find_element(Locator.BUTTON_DELIVERY)
            .click())


    def verify_new_advert(self):
        """Closes pop-up windows and returns text value of newly created advert."""
        element = self.find_element(Locator.dialog1).click()
        element = self.find_element(Locator.dialog2).click()
        element = self.find_element(Locator.advert_title)
        self.wait(3)
        return element.get_attribute("text")
