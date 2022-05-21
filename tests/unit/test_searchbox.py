import pytest

from pages.home_page import PageHome
from pages.login_page import PageLogin


@pytest.mark.usefixtures("setup", "logger")
class TestSearchbox:

    @pytest.fixture()
    def class_setup(self):
        self.page_home = PageHome(self.driver)
        self.page_login = PageLogin(self.driver)


    @pytest.mark.order(1)
    def test_searchbox_phrase_one(self, class_setup):
        self.page_login.accept_privacy_dialog()
        self.logger.info('Searching for phrase...:')
        self.page_home.search_phrase(phrase_to_search='Drukarka', location='Gdańsk')
        assert "Drukarka w Gdańsk" in self.driver.title, "Assertion Failed"