#coding: utf-8
from email.policy import default
import pytest
import utils.helpers as helpers

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager


#@pytest.fixture(params=["edge", "safari"], scope='class')
@pytest.fixture(scope='class')
def setup(request, browser, url):
#def setup(request):
    if browser == "edge":
        driver = webdriver.Edge(service = Service(EdgeChromiumDriverManager().install()))
    elif browser == "chrome":
        driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
    elif browser == "safari":
        driver = webdriver.Safari(service = Service(executable_path='/usr/bin/safaridriver'))

    #driver.get(url)
    driver.get(helpers.base_url)
    driver.maximize_window()
    request.cls.driver = driver
    
    yield driver
    driver.quit()


#this will get the value of CLI/Hooks
def pytest_addoption(parser):
    parser.addoption("--browser", default="safari")
    parser.addoption("--url")


#This will return the browser value to setup method
@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


#This will return the url value to setup method
@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")