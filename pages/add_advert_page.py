import time
import utils.globals as globals

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class PageAddAdvert:

    textfield_title = '//textarea[@data-cy="posting-title"]'
    button_category = '//div[@data-cy="posting-select-category"]'
    button_suggested_category = '//button[@data-cy="posting-suggested-categories-item"]'
    textfield_description = '//textarea[@name="description"]'
    textfield_price = 'parameters.price.price'
    button_free = '//button[text()="Za darmo"]'
    button_exchange = '//button[text()="Zamienię"]'
    button_type_private = '//button[text()="Prywatne"]'
    button_type_business = '//button[text()="Firmowe"]'
    button_item_condition = '//button[@placeholder="Wybierz"]'
    location = '//input[@data-cy="location-search-input"]'
    switch_delivery = '//h6[text()="Dodaj Przesyłkę OLX"]'
    submit_button = '//button[@type="submit"]'


    def __init__(self, driver):
        self.driver = driver
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
        try:
            element = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, self.textfield_title))
            )
            element.send_keys(self._advert.get('title'))
        except TimeoutException as Exception:
            print("Element not found in desired time")
            raise Exception


    def fill_in_suggested_category(self):
        """Opens category tray, waits for suggested category to appear and chooses it."""
        try:
            self.driver.find_element(By.XPATH, self.button_category).click()
            element = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, self.button_suggested_category))
            )
            element.click()
        except TimeoutException as Exception:
            print("Element not found in desired time")
            raise Exception


    def upload_photos(self):
        """Safari unsupported. Uploads photos from test data gallery."""
        for i in range(1, 4):
            self.driver.find_element(
                By.ID, "photo-attachment-files").send_keys(globals.ROOT_DIR + f"/data/gallery/{i}.jpg"
            )


    def fill_in_description(self):
        """Searches for description form field and fills a value in."""
        self.driver.execute_script("window.scrollTo(0, 850)")
        try:
            element = self.driver.find_element(By.XPATH, self.textfield_description)
            element.send_keys(self._advert.get('description'))
        except NoSuchElementException as Exception:
            print("Element not found in desired time")
            raise Exception


    def fill_in_additional_info(self):
        """Searches for item condition dropdown list and chooses specific option."""
        self.check_price_value()
        self.check_advert_type()
        self.driver.find_element(By.XPATH, self.button_item_condition).click()
        try: 
            option = self._advert.get('item_condition')
            element = self.driver.find_element(
                By.XPATH, f"//*[@id='posting-form']/main/div[1]/div[4]/div[2]/ul/li[2]/div/div/ul/li[{option}]"
            )
            element.click()
        except NoSuchElementException as Exception:
            print("Element not found in desired time")
            raise Exception   


    def fill_in_contact_info(self):
        """Searches for contact location form field and fills a value in."""
        element = self.driver.find_element(By.XPATH, self.location)
        element.clear()
        element = self.driver.find_element(By.XPATH, self.location).send_keys(self._advert.get('location'))
        try:
            element = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((
                    By.XPATH, "//*[@id='posting-form']/main/div[1]/div[7]/div[2]/div/div/div/div/div/div/div[2]/li"
                ))
            )
            element.click()
        except TimeoutException as Exception:
            print("Element not found in desired time")
            raise Exception


    def preview_advert(self):
        """Redirects to new page containing pre-view of new advert."""
        pass


    def submit_advert(self):
        """Redirects to confirmation page and creates new advert."""
        self.driver.find_element(By.XPATH, self.submit_button).click()
        time.sleep(3)


    def check_price_value(self):
        """
        Checks if string stored in price key is digit and if so fills form field.
        Otherwise selects for free or exchange options.
        """
        price = self._advert.get('price')
        if price.isdigit():
            self.driver.find_element(By.ID, self.textfield_price).send_keys(self._advert.get('price'))
        elif price == "free":
            self.driver.find_element(By.XPATH, self.button_free).click()
        elif price == "exchange":
            self.driver.find_element(By.XPATH, self.button_exchange).click()

    
    def check_advert_type(self):
        """
        Checks if string stored in advert type key is private or business.
        Selects proper type of advert.
        """
        type = self._advert.get('advert_type')
        if type == "private":
            self.driver.find_element(By.XPATH, self.button_type_private).click()
        elif type == "business":
            self.driver.find_element(By.XPATH, self.button_type_business).click()


    def disable_delivery(self):
        """Disables option for integrated delivery system."""
        self.driver.execute_script("window.scrollTo(0, 1800)")
        try:
            element = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, self.switch_delivery))
            )
            element.click()
        except TimeoutException as Exception:
            print("Element not found in desired time")
            raise Exception


    def verify_new_advert(self):
        """Closes pop-up windows and returns text value of newly created advert."""
        try:
            element = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div[2]/button'))).click()
            element = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div/footer/button/span/span'))).click()
            element = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div/div[2]/div/div[1]/div[2]/div[1]/h5/a')))
            time.sleep(3)
            return element.get_attribute("text")
        except TimeoutException as Exception:
            print("Element not found in desired time")
            raise Exception