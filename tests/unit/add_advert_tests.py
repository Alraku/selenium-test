import pytest
import utils.globals as globals

from pages.login_page import PageLogin
from pages.add_advert_page import PageAddAdvert
from utils.helpers import CookieOperations


@pytest.mark.usefixtures("setup", "logger")
class TestAddAdvert:

    @pytest.fixture()
    def class_setup(self):
        self.driver.get(globals.BASE_URL)
        CookieOperations.load_cookie(self.driver)
        self.page_add_advert = PageAddAdvert(self.driver)
        self.driver.get(globals.BASE_URL + '/nowe-ogloszenie')


    @pytest.mark.order(1)
    def test_add_advert_basic(self, class_setup):
        #self.page_add_advert.close_confirmation_dialog()
        self.page_add_advert.fill_in_fields('Smartphone Iphone 13 Pro - Nowy, gwarancja',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris gravida quam eget ligula erat curae.')
        self.page_add_advert.submit_advert()
