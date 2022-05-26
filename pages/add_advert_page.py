import time
import utils.globals as globals
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


LOGGER = logging.getLogger(__name__)

class PageAddAdvert:

    textfield_title = '//*[@id="posting-form"]/main/div[1]/div[1]/div[1]/div/div/div/div/textarea'
    button_category = '//*[@id="posting-form"]/main/div[1]/div[1]/div[2]/div'
    button_suggested_category = '//*[@id="posting-form"]/main/div[1]/div[1]/div[2]/div/div[2]/div/div/button'
    textfield_description = '//textarea[@name="description"]'
    textfield_price = 'parameters.price.price'
    button_free = '//*[@id="posting-form"]/main/div[1]/div[4]/div[1]/div/div/div[1]/button[2]'
    button_exchange = '//*[@id="posting-form"]/main/div[1]/div[4]/div[1]/div/div/div[1]/button[3]'
    button_type_private = '//*[@id="posting-form"]/main/div[1]/div[4]/div[2]/ul/li[1]/div/div/div[1]/button'
    button_type_business = '//*[@id="posting-form"]/main/div[1]/div[4]/div[2]/ul/li[1]/div/div/div[2]/button'
    button_item_condition = '//*[@id="posting-form"]/main/div[1]/div[4]/div[2]/ul/li[2]/div/div/div/button[1]'
    location = 'city_id'
    contact_person = 'person'
    switch_delivery = '//*[@id="posting-form"]/main/div[1]/div[5]/div/div/div[1]/label/h6'
    submit_button = '//*[@id="posting-form"]/main/div[1]/div[8]/div/button[2]'


    def __init__(self, driver):
        self.driver = driver
        self._advert = None


    def fill_in_fields(self):
        self.fill_in_title()
        self.fill_in_suggested_category()
        self.fill_in_description()
        self.fill_in_additional_info()
        self.fill_in_contact_info()
        self.disable_delivery()


    def fill_in_title(self):
        try:
            element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, self.textfield_title)))
            element.send_keys(self._advert.get('title'))
        except TimeoutException as Exception:
            print("Element not found in desired time")
            raise Exception


    def fill_in_suggested_category(self):
        try:
            # Select category button and choose suggested category 
            self.driver.find_element(By.XPATH, self.button_category).click()
            element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, self.button_suggested_category)))
            element.click()
        except TimeoutException as Exception:
            print("Element not found in desired time")
            raise Exception


    def upload_photos(self):
        for i in range(1, 4):
            self.driver.find_element(By.ID, "photo-attachment-files").send_keys(globals.ROOT_DIR + f"/data/gallery/{i}.jpg")


    def fill_in_description(self):
        self.driver.execute_script("window.scrollTo(0, 850)")
        try:
            element = self.driver.find_element(By.XPATH, self.textfield_description)
            element.send_keys(self._advert.get('description'))
        except NoSuchElementException as Exception:
            print("Element not found in desired time")
            raise Exception


    def fill_in_additional_info(self):
        self.check_price_value()
        self.check_advert_type()
        # Choose item condition from dropdown list
        self.driver.find_element(By.XPATH, self.button_item_condition).click()
        try: 
            option = self._advert.get('item_condition')
            element = self.driver.find_element(By.XPATH, f"//*[@id='posting-form']/main/div[1]/div[4]/div[2]/ul/li[2]/div/div/ul/li[{option}]")
            element.click()
        except NoSuchElementException as Exception:
            print("Element not found in desired time")
            raise Exception   


    def fill_in_contact_info(self):
        element = self.driver.find_element(By.NAME, self.location)
        element.clear()
        element = self.driver.find_element(By.NAME, self.location).send_keys(self._advert.get('location'))


    def preview_advert(self):
        pass


    def submit_advert(self):
        self.driver.find_element(By.XPATH, self.submit_button).click()


    def close_confirmation_dialog(self):
        element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "css-spwpto")))
        element.click()


    def check_price_value(self):
        price = self._advert.get('price')
        # If price is digit then fill in value, else choose option
        if price.isdigit():
            self.driver.find_element(By.ID, self.textfield_price).send_keys(self._advert.get('price'))
        elif price == "free":
            self.driver.find_element(By.XPATH, self.button_free).click()
        elif price == "exchange":
            self.driver.find_element(By.XPATH, self.button_exchange).click()

    
    def check_advert_type(self):
        type = self._advert.get('advert_type')
        # Choose private or business type of advert
        if type == "private":
            self.driver.find_element(By.XPATH, self.button_type_private).click()
        elif type == "business":
            self.driver.find_element(By.XPATH, self.button_type_business).click()


    def disable_delivery(self):
        self.driver.execute_script("window.scrollTo(0, 1800)")
        try:
            element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, self.switch_delivery)))
            element.click()
        except TimeoutException as Exception:
            print("Element not found in desired time")
            raise Exception


    @property
    def advert(self):
        return self._advert


    @advert.setter
    def advert(self, advert):
        self._advert = advert