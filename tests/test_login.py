import pytest
import time
import helpers

from selenium.webdriver.common.by import By
from pages.login_page import PageLogin

@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.fixture(autouse = True)
    def class_setup(self):
        self.page_login = PageLogin(self.driver)
        self.page_login.driver.get(helpers.base_url + '/konto')


    @pytest.mark.order(1)
    def test_login_user(self):
        self.page_login.accept_privacy_dialog()
        self.page_login.enter_credentials(helpers.test_username, helpers.test_password)
        self.page_login.click_login_button()
        assert "Mój OLX" in self.driver.title, "Assertion Failed"
