import pytest
import logging
import utils.globals as globals

from pages.login import PageLogin
from utils.helpers import CookieOperations

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.fixture()
    def class_setup(self):
        self.page_login = PageLogin(self.driver)
        self.driver.get(globals.BASE_URL + '/konto')


    @pytest.mark.order(1)
    def test_login_valid_user(self, class_setup):
        logger.info("Test execution started.")
        self.page_login.accept_privacy_dialog()
        self.page_login.enter_credentials(globals.TEST_EMAIL, globals.TEST_PASSWORD)
        self.page_login.click_login_button(timeout = 5)
        CookieOperations.save_cookie(self.driver)
        assert "/mojolx" in self.driver.current_url, logger.error("Assertion failed, address doesn't match.")


    @pytest.mark.order(2)
    def test_login_invalid_user(self, class_setup):
        self.page_login.accept_privacy_dialog()
        self.page_login.enter_credentials('bademail@email.com', 'badpassword')
        self.page_login.click_login_button(timeout = 5)
        assert self.page_login.check_invalid_login_label(), logger.error("Assertion failed, text of the element doesn't match.")


    @pytest.mark.order(3)
    def test_login_with_saved_cookie(self):
        self.driver.get(globals.BASE_URL)
        CookieOperations.load_cookie(self.driver)
        self.driver.get(globals.BASE_URL + '/konto')
        assert "/mojolx" in self.driver.current_url, logger.error("Assertion failed, address doesn't match.")

        