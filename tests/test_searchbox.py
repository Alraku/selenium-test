import pytest

from pages.home_page import PageHome
from pages.login_page import PageLogin


@pytest.mark.usefixtures("setup")
class TestSeachbox:

    @pytest.fixture()
    def class_setup(self):
        self.page_home = PageHome(self.driver)
        self.page_login = PageLogin(self.driver)


    @pytest.mark.order(1)
    def test_seachbox_one(self, class_setup):
        self.page_login.accept_privacy_dialog()
        self.page_home.search_phrase(phrase_to_search='Sony A6300', location='Gdańsk')
        assert "Sony A6300 w Gdańsk" in self.driver.title, "Assertion Failed"