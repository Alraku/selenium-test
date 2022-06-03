import pytest
import utils.globals as globals

from selenium.webdriver.common.by import By
from pages.login_page import PageLogin
from utils.helpers import CookieOperations


@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.fixture()
    def class_setup(self):
        self.page_login = PageLogin(self.driver)
        self.page_login.driver.get(globals.BASE_URL + '/konto')


    @pytest.mark.order(1)
    def test_login_valid_user(self, class_setup):
        self.page_login.accept_privacy_dialog()
        self.page_login.enter_credentials(globals.TEST_EMAIL, globals.TEST_PASSWORD)
        self.page_login.click_login_button(timeout = 5)
        CookieOperations.save_cookie(self.driver)
        assert "Mój OLX" in self.driver.title, "Assertion Failed"


    @pytest.mark.order(2)
    def test_login_invalid_user(self, class_setup):
        self.page_login.accept_privacy_dialog()
        self.page_login.enter_credentials('bademail@email.com', 'badpassword')
        self.page_login.click_login_button(timeout = 5)
        #TODO: przeniesc do POMa
        invalid_data_label = self.driver.find_element(By.XPATH, '//label[@for="userPass" and @class="error"]')
        assert "Nieprawidłowy login lub hasło" == invalid_data_label.text


    @pytest.mark.order(3)
    def test_login_with_saved_cookie(self):
        CookieOperations.load_cookie(self.driver)
        self.driver.get(globals.BASE_URL + '/konto')
        assert "Mój OLX" in self.driver.title, "Assertion Failed"

        