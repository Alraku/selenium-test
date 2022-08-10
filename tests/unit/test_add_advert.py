import pytest
import utils.globals as globals

from pages.page_add_advert import PageAddAdvert
from pages.page_login import PageLogin
from pages.page_home import PageHome
from data.test_data import testdata_advert_form_fields


@pytest.mark.usefixtures("setup")
class TestAddAdvert(object):

    @pytest.fixture()
    def class_setup(self):
        self.page_login = PageLogin(self.driver)
        self.page_home = PageHome(self.driver)
        self.page_add_advert = PageAddAdvert(self.driver)
        self.page_login.load_cookie()
        self.driver.get(globals.BASE_URL)
        self.page_home.click_add_advert()
        # self.driver.get(globals.BASE_URL + '/nowe-ogloszenie')

    @pytest.mark.order(1)
    @pytest.mark.parametrize('advert', testdata_advert_form_fields)
    def test_add_advert_basic(self, class_setup, advert):
        self.page_add_advert.advert = advert
        self.page_add_advert.fill_in_fields()
        self.page_add_advert.submit_advert()
        self.driver.get(globals.BASE_URL + '/mojolx/waiting/')
        assert self.page_add_advert.verify_new_advert() == advert.get('title')