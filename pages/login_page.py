import time
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

logger = logging.getLogger(__name__)

class PageLogin:

    textfield_username = '//*[@id="userEmail"]'
    textfield_password = '//*[@id="userPass"]'
    sign_in_button = '//*[@id="se_userLogin"]'
    privacy_dialog_button = '//*[@id="onetrust-accept-btn-handler"]'
    label_invalid_cred = '//label[@for="userPass" and @class="error"]'

    cookie_path = "/../utils/cookies/cookies.pkl"


    def __init__(self, driver):
        self.driver = driver

    
    def enter_credentials(self, username: str, password: str):
        logger.info("Entering credentials in login form.")
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((
                    By.XPATH, self.textfield_username))).send_keys(username)

            element = self.driver.find_element(
                By.XPATH, self.textfield_password).send_keys(password)

        except TimeoutException as Exception:
            print("Element not found in desired time")
            raise Exception


    def click_login_button(self, timeout: int = 3):
        logger.info("Clicking login button.")
        element = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((
                    By.XPATH, self.sign_in_button)))
        element.click()
        time.sleep(timeout)


    def accept_privacy_dialog(self):
        logger.info("Accepting privacy dialog.")
        try:
            element = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((
                    By.XPATH, self.privacy_dialog_button)))
            element.click()

        except TimeoutException as Exception:
            print("Element not found in desired time")
            raise Exception


    def check_invalid_login_label(self):
        try:
            element = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((
                    By.XPATH, self.label_invalid_cred)))
            return element.text == "Nieprawidłowy login lub hasło"

        except TimeoutException as Exception:
            print("Element not found in desired time")
            raise Exception
