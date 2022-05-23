import time
import pytest
import utils.globals as globals

from pages.home_page import PageHome
from pages.login_page import PageLogin
from data.test_data import testdata_searchbox
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup", "logger")
class TestSearchbox:

    @pytest.fixture()
    def class_setup(self):
        self.page_home = PageHome(self.driver)
        self.page_login = PageLogin(self.driver)
        self.driver.get(globals.base_url)


    @pytest.mark.order(1)
    @pytest.mark.parametrize("data_search_term, data_location, data_result", testdata_searchbox)
    def test_searchbox_term_one(self, class_setup, data_search_term, data_location, data_result):
        self.page_login.accept_privacy_dialog()
        self.page_home.search_phrase(search_term=data_search_term, location=data_location)
        assert data_result in self.driver.title, "Assertion Failed - Title does not match"


    @pytest.mark.order(2)
    def test_search_in_descriptions(self, class_setup):
        self.page_login.accept_privacy_dialog()
        self.page_home.search_phrase(search_term="Vintage", location="Toruń")
        no_of_adverts = self.driver.find_element(By.CSS_SELECTOR, "div[data-testid='total-count']").text
        number1 = int("".join(filter(str.isdigit, no_of_adverts)))
        self.logger.info(number1)
        self.driver.find_element(By.ID, "description").click()
        time.sleep(3)
        no_of_adverts = self.driver.find_element(By.CSS_SELECTOR, "div[data-testid='total-count']").text
        number2 = int("".join(filter(str.isdigit, no_of_adverts)))
        self.logger.info(number2)
        assert number2 >= number1, "Assertion Failed - Number is not greater or equal"
        