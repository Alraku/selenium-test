import pytest
import time

from pages.login_page import PageLogin

@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.fixture(autouse = True)
    def class_setup(self):
        self.t1 = PageLogin(self.driver)


    @pytest.mark.order(1)
    def test_login(self):
        self.t1.enter_user_name("testuser")
        time.sleep(2)


    @pytest.mark.order(2)
    def test_website_title(self):
        assert "Login" in self.driver.title, "Assertion Failed"