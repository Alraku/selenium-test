import pytest
import utils.globals as globals

from pages.page_login import PageLogin
from pages.page_add_advert import PageAddAdvert
from data.test_data import testdata_advert_form_fields


@pytest.mark.usefixtures("setup")
class TestAddAdvert(object):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.page_login = PageLogin(self.driver)
        self.page_add_advert = PageAddAdvert(self.driver)
        self.page_login.load_cookie()
        self.page_add_advert.open()

    @pytest.mark.parametrize('advert', testdata_advert_form_fields)
    def test_add_advert(self, advert):
        self.page_add_advert.fill_in(advert)
        self.page_add_advert.submit()
        self.driver.get(globals.BASE_URL + '/mojolx/waiting/')
        assert self.page_add_advert.is_advert_visible()
