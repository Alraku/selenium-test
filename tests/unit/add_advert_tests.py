import pytest
import utils.globals as globals
import time

from pages.add_advert_page import PageAddAdvert
from utils.helpers import CookieOperations
from data.test_data import testdata_advert_form_fields


@pytest.mark.usefixtures("setup", "logger")
class TestAddAdvert:

    @pytest.fixture()
    def class_setup(self):
        self.driver.get(globals.BASE_URL)
        CookieOperations.load_cookie(self.driver)
        self.page_add_advert = PageAddAdvert(self.driver)
        self.driver.get(globals.BASE_URL + '/nowe-ogloszenie')


    @pytest.mark.order(1)
    @pytest.mark.parametrize('advert', testdata_advert_form_fields)
    def test_add_advert_basic(self, class_setup, advert):
        #self.page_add_advert.close_confirmation_dialog()
        self.page_add_advert.advert = advert
        self.page_add_advert.fill_in_fields()
        self.page_add_advert.submit_advert()
        time.sleep(5)