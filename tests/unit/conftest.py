#coding: utf-8
import pytest
import logging
import utils.globals as globals

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager


#@pytest.fixture(params=["edge", "safari"], scope='class')
@pytest.fixture(scope='class')
def setup(request, browser, url):
    if browser == "edge":
        driver = webdriver.Edge(service = Service(EdgeChromiumDriverManager().install()))
    elif browser == "chrome":
        driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
    elif browser == "safari":
        driver = webdriver.Safari(service = Service(executable_path='/usr/bin/safaridriver'))

    driver.maximize_window()
    request.cls.driver = driver
    
    yield driver
    driver.quit()


@pytest.fixture(scope='class')
def logger(request):
    logger = logging.getLogger(__name__)
    request.cls.logger = logger
    return logger


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