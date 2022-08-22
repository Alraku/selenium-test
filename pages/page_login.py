from pages._base import BasePage
from pages._locators import PageLoginLocators as Locator
from tests._webdriver import WebDriver


class PageLogin(BasePage):

    def __init__(self, driver) -> None:
        super().__init__(driver, '/konto')
        self.driver = driver

    def enter_credentials(self, username: str, password: str) -> None:
        """
        Enters user credentials (username and password) into the form.

        Args:
            username (str): user's login (e-mail)
            password (str): user's password
        """
        self.logger.info("Entering credentials in login form.")
        self.find_element(Locator.INPUT_USERNAME).send_keys(username)
        self.find_element(Locator.INPUT_PASSWORD).send_keys(password)

    def click_login_button(self) -> None:
        """
        Clicks login button and waits 5 seconds to refresh page.
        """
        self.logger.info("Clicking login button.")
        self.find_element(Locator.BUTTON_SIGN_IN).click()
        self.wait(5)

    def accept_privacy_dialog(self) -> None:
        """
        If privacy dialogue appears, clicks it.
        """
        self.logger.info("Accepting privacy dialog.")
        try:
            self.find_element(Locator.BUTTON_PRIVACY_ACCEPT).click()
        except BaseException:
            self.logger.warning("Privacy Dialog did not appear.")

    def is_logged_in(self) -> bool:
        """
        Checks if URL says that user is logged in.

        Returns:
            bool: Value that says if user is logged in or not.
        """
        self.logger.info("Checking if user is logged in.")
        if "/mojolx" in self.driver.current_url:
            WebDriver.save_cookie(self.driver)
            self.logger.info("User is logged in.")
            return True
        else:
            self.logger.error("Login operation failed.")
            return False

    def is_login_invalid(self) -> bool:
        """
        Checks if invalid login credential label appears.

        Returns:
            bool: Value that says if login was invalid or not.
        """
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
        """
        Wrapping function for loading cookies in WebDriver instance.
        """
        WebDriver.load_cookie(self.driver)
