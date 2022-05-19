import pytest
import utils.helpers as helpers

from selenium.webdriver.common.by import By
from pages.login_page import PageLogin


@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.fixture()
    def class_setup(self):
        self.page_login = PageLogin(self.driver)
        self.page_login.driver.get(helpers.base_url + '/konto')


    @pytest.mark.order(1)
    def test_login_valid_user(self, class_setup):
        self.page_login.accept_privacy_dialog()
        self.page_login.enter_credentials(helpers.test_email, helpers.test_password)
        self.page_login.click_login_button(timeout = 5)
        self.page_login.save_cookie()
        assert "Mój OLX" in self.driver.title, "Assertion Failed"


    @pytest.mark.order(2)
    def test_login_invalid_user(self, class_setup):
        self.page_login.accept_privacy_dialog()
        self.page_login.enter_credentials('bademail@email.com', 'badpassword')
        self.page_login.click_login_button(timeout = 5)
        invalid_data_label = self.driver.find_element(By.XPATH, '//label[@for="userPass" and @class="error"]')
        assert "Nieprawidłowy login lub hasło" == invalid_data_label.text


    @pytest.mark.order(3)
    def test_login_cookie(self):
        self.page_login = PageLogin(self.driver)
        self.page_login.load_cookie()
        self.page_login.driver.get(helpers.base_url + '/konto')
        assert "Mój OLX" in self.driver.title, "Assertion Failed"

        