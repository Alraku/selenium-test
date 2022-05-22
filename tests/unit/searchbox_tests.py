import pytest

from pages.home_page import PageHome
from pages.login_page import PageLogin
import utils.globals as globals

testdata = [
    ("Drukarka", "Gdańsk", "Drukarka w Gdańsk"),
    ("Aparat", "Toruń", "Aparat w Toruń")
]

@pytest.mark.usefixtures("setup", "logger")
class TestSearchbox:

    @pytest.fixture()
    def class_setup(self):
        self.page_home = PageHome(self.driver)
        self.page_login = PageLogin(self.driver)
        self.driver.get(globals.base_url)


    @pytest.mark.order(1)
    @pytest.mark.parametrize("data_search_term, data_location, data_result", testdata)
    def test_searchbox_term_one(self, class_setup, data_search_term, data_location, data_result):
        self.page_login.accept_privacy_dialog()
        self.page_home.search_phrase(search_term=data_search_term, location=data_location)
        assert data_result in self.driver.title, "Assertion Failed - Title does not match"