import time
import utils.globals as globals

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class PageAddAdvert:

    title = 'textarea[data-testid="posting-title"]'
    description = '//textarea[@name="description"]'
    location = 'city_id'
    contact_person = 'person'
    submit_button = '//button[@type="submit"]'


    def __init__(self, driver):
        self.driver = driver


    def fill_in_fields(self, title, description):
        self.fill_in_title(title)
        self.select_category()
        #self.upload_photos()
        self.fill_in_description(description)
        self.fill_in_contact_info('Gdańsk', 'Test Automation')
        time.sleep(5)


    def fill_in_title(self, title):
        self.driver.find_element(By.CSS_SELECTOR, self.title).send_keys(title)


    def select_category(self):
        try:
            #klikniecie w wybór kategorii
            element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, "css-hncutm")))
            element.click()
            #klikniecie podpowiedzianej kategorii
            element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, "css-1ujjrsn")))
            element.click()
            #zamkniecie okna wyboru kategorii
            #element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, "css-spwpto")))
            #element.click()
        except TimeoutException as Exception:
            print("Element not found in desired time")
            raise Exception


    def upload_photos(self):
        for i in range(1, 4):
            self.driver.find_element(By.ID, "photo-attachment-files").send_keys(globals.ROOT_DIR + f"/data/gallery/{i}.jpg")
        time.sleep(5)


    def fill_in_description(self, description):
        desc = self.driver.find_element(By.XPATH, self.description)
        self.driver.execute_script("window.scrollTo(0, 700)") 
        desc.send_keys(description)


    def fill_in_contact_info(self, location, contact_person):
        self.driver.find_element(By.NAME, self.location).send_keys(location)
        #self.driver.find_element(By.ID, self.contact_person).send_keys(contact_person)


    def preview_advert(self):
        pass


    def submit_advert(self):
        self.driver.find_element(By.XPATH, self.submit_button).click()


    def close_confirmation_dialog(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "css-spwpto")))
        element.click()