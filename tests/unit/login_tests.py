import pytest
import utils.globals as globals

from utils.logger import logger
from pages.login_page import PageLogin
from utils.helpers import CookieOperations


@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.fixture()
    def class_setup(self):
        self.page_login = PageLogin(self.driver)
        self.driver.get(globals.BASE_URL + '/konto')


    @pytest.mark.order(1)
    def test_login_valid_user(self, class_setup):
        logger.step("Test execution started.")
        self.page_login.accept_privacy_dialog()
        self.page_login.enter_credentials(globals.TEST_EMAIL, globals.TEST_PASSWORD)
        self.page_login.click_login_button(timeout = 5)
        CookieOperations.save_cookie(self.driver)
        assert "/mojolx" in self.driver.current_url, "Assertion failed, address doesn't match."


    @pytest.mark.order(2)
    def test_login_invalid_user(self, class_setup):
        self.page_login.accept_privacy_dialog()
        self.page_login.enter_credentials('bademail@email.com', 'badpassword')
        self.page_login.click_login_button(timeout = 5)
        assert self.page_login.check_invalid_login_label(), "Assertion failed, text of the element doesn't match."


    @pytest.mark.order(3)
    def test_login_with_saved_cookie(self):
        self.driver.get(globals.BASE_URL)
        CookieOperations.load_cookie(self.driver)
        self.driver.get(globals.BASE_URL + '/konto')
        assert "/mojolx" in self.driver.current_url, "Assertion failed, address doesn't match."

        