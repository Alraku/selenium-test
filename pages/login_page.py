import time
import logging
from framework.wrappers import find_element
from pages._locators import LoginPageLocators as Locator

logger = logging.getLogger(__name__)


class PageLogin:

    def __init__(self, driver):
        self.driver = driver

    
    def enter_credentials(self, username: str, password: str):
        logger.info("Entering credentials in login form.")
        textfield_username = (find_element(
            self.driver, Locator.INPUT_USERNAME)
            .send_keys(username))

        textfield_password = (find_element(
            self.driver, Locator.INPUT_PASSWORD)
            .send_keys(password))


    def click_login_button(self, timeout: int = 3):
        logger.info("Clicking login button.")
        login_button = (find_element(
            self.driver, Locator.BUTTON_SIGN_IN)
            .click())
        time.sleep(timeout)


    def accept_privacy_dialog(self):
        logger.info("Accepting privacy dialog.")
        try:
            dialog = (find_element(
                self.driver, Locator.BUTTON_PRIVACY_ACCEPT)
                .click())
        except:
            logger.warning("Privacy Dialog did not appear.")


    def check_invalid_login_label(self):
        logger.info("Looking for invalid login credentials label.")
        label = find_element(self.driver, Locator.LABEL_INVALID_CREDS)
        return label.text == "Nieprawidłowy login lub hasło"
