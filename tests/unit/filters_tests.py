import pytest

from pages.home_page import PageHome
from utils.globals import globals


@pytest.mark.usefixtures("setup")
class TestFilters:

    @pytest.fixture()
    def class_setup(self):
        self.home_page = PageHome(self.driver)
        self.driver.get(globals.base_url)
