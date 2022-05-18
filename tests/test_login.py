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
    def test_login(self):
        self.page_login.accept_privacy_dialog()
        self.page_login.enter_credentials('testingautomation@protonmail.com', '!qW3Er5%y78i')
        self.page_login.click_login_button()
        time.sleep(10)


    @pytest.mark.order(2)
    def test_website_title(self):
        assert "Ogłoszenia" in self.driver.title, "Assertion Failed"