from pages._base import BasePage
from pages._locators import PageLoginLocators as Locator


class PageLogin(BasePage):

    def __init__(self, driver) -> None:
        super().__init__(driver, '/konto')


    def enter_credentials(self, username: str, password: str) -> None:
        self.logger.info("Entering credentials in login form.")
        textfield_username = (self.find_element(Locator.INPUT_USERNAME)
            .send_keys(username))

        textfield_password = (self.find_element(Locator.INPUT_PASSWORD)
            .send_keys(password))


    def click_login_button(self) -> None:
        self.logger.info("Clicking login button.")
        login_button = (self.find_element(Locator.BUTTON_SIGN_IN)
            .click())
        self.wait(3)


    def accept_privacy_dialog(self) -> None:
        self.logger.info("Accepting privacy dialog.")
        try:
            dialog = (self.find_element(Locator.BUTTON_PRIVACY_ACCEPT)
                .click())
        except:
            self.logger.warning("Privacy Dialog did not appear.")


    def check_invalid_login_label(self) -> bool:
        self.logger.info("Looking for invalid login credentials label.")
        label = self.find_element(Locator.LABEL_INVALID_CREDS)
        return label.text
