#coding: utf-8
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class TestClass:

    @pytest.fixture(params=["edge", "safari"], scope='class')
    def driver(self, request):
        if request.param == "edge":
            driver = webdriver.Edge(service = Service(EdgeChromiumDriverManager().install()))
        if request.param == "safari":
            driver = webdriver.Safari(service = Service(executable_path='/usr/bin/safaridriver'))

        yield driver
        driver.quit()


    @pytest.mark.order(2)
    def test_check_website_title(self, driver):
        driver.get("https://www.onet.pl")
        print(driver.title)
        assert "Onet" in driver.title, "Assertion Failed"


    @pytest.mark.order(1)
    def test_check_website_title_2(self, driver):
        driver.get("https://www.google.com")
        print(driver.title)
        assert "Google" in driver.title, "Assertion Failed"