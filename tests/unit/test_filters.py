import pytest
import logging

from pages.home import PageHome
from utils.globals import globals

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("setup")
class TestFilters:

    @pytest.fixture()
    def class_setup(self):
        self.home_page = PageHome(self.driver)
        self.driver.get(globals.base_url)
