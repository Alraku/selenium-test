import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    driver.get("https://www.onet.pl")

    yield
    driver.quit()


def test_method(test_setup):
    x = 5
    y = 2
    # assert x + y == 7, "Assertion failed, Expected 7"
    print(driver.title)
    assert "Onet" in driver.title, "Assertion Failed"
