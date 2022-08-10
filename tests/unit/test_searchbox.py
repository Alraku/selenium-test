import pytest

from pages.page_home import PageHome
from pages.page_login import PageLogin
from pages.page_results import PageResults
from data.test_data import testdata_searchbox


@pytest.mark.usefixtures("setup")
class TestSearchbox(object):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.page_home = PageHome(self.driver)
        self.page_login = PageLogin(self.driver)
        self.page_results = PageResults(self.driver)
        self.page_home.open()

    @pytest.mark.parametrize("phrase, location, result", testdata_searchbox)
    def test_searchbox(self, phrase, location, result):
        self.page_login.accept_privacy_dialog()
        self.page_home.search_phrase(phrase, location)
        assert self.page_results.check_result(result)

    def test_search_in_descriptions(self):
        self.page_login.accept_privacy_dialog()
        self.page_home.search_phrase("Vintage", "Toruń")
        self.page_results.click_checkbox('description')
        assert self.page_results.has_element_reloaded()
