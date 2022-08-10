import pytest

from pages.page_home import PageHome


@pytest.mark.usefixtures("setup")
class TestFilters:

    @pytest.fixture()
    def class_setup(self):
        self.home_page = PageHome(self.driver)
