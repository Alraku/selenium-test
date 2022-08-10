from pages._base import BasePage
from pages._locators import PageLoginLocators as Locator
from utils.helpers import CookieOperations


class PageLogin(BasePage):

    def __init__(self, driver) -> None:
        super().__init__(driver, '/konto')
        self.driver = driver

    def enter_credentials(self, username: str, password: str) -> None:
        self.logger.info("Entering credentials in login form.")
        self.find_element(Locator.INPUT_USERNAME).send_keys(username)
        self.find_element(Locator.INPUT_PASSWORD).send_keys(password)

    def click_login_button(self) -> None:
        self.logger.info("Clicking login button.")
        self.find_element(Locator.BUTTON_SIGN_IN).click()
        self.wait(5)

    def accept_privacy_dialog(self) -> None:
        self.logger.info("Accepting privacy dialog.")
        try:
            self.find_element(Locator.BUTTON_PRIVACY_ACCEPT).click()
        except:
            self.logger.warning("Privacy Dialog did not appear.")
            
    def is_logged_in(self) -> bool:
        self.logger.info("Checking if user is logged in.")
        if "/mojolx" in self.driver.current_url:
            CookieOperations.save_cookie(self.driver)
            self.logger.info("User is logged in.")
            return True
        else:
            self.logger.error("Login operation failed.")
            return False

    def is_invalid_login(self) -> bool:
        self.logger.info("Looking for invalid login credentials label.")
        expected = "Nieprawidłowy login lub hasło"
        actual = self.find_element(Locator.LABEL_INVALID_CREDS)

        if actual.text == expected:
            self.logger.info("Invalid login detected.")
            return True
        else:
            self.logger.error(
                f"Assertion Failed, expected: {expected}, actual: {actual}")
            return False

    def load_cookie(self) -> None:
        CookieOperations.load_cookie(self.driver)
        self.wait(3)
