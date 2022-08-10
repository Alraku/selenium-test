import pytest
import utils.globals as globals

from pages.page_login import PageLogin


@pytest.mark.usefixtures("setup")
class TestLogin(object):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.page_login = PageLogin(self.driver)
        self.page_login.open()

    def test_login(self):
        self.page_login.accept_privacy_dialog()
        self.page_login.enter_credentials(
            globals.TEST_EMAIL, globals.TEST_PASSWORD)

        self.page_login.click_login_button()
        assert self.page_login.is_logged_in()

    def test_login_invalid(self):
        self.page_login.accept_privacy_dialog()
        self.page_login.enter_credentials(
            'bademail@email.com', 'badpassword')

        self.page_login.click_login_button()
        assert self.page_login.is_invalid_login()

    def test_login_cookie(self):
        self.page_login.load_cookie()
        self.page_login.open()
        assert self.page_login.is_logged_in()
