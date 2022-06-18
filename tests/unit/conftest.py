#coding: utf-8
import pytest
import utils.globals as globals


from utils.logger import logger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.safari.options import Options as SafariOptions


#@pytest.fixture(params=["edge", "safari"], scope='class')
@pytest.fixture(scope='class')
def setup(request, browser, url):
    if browser == "edge":
        driver = webdriver.Edge(service = Service(EdgeChromiumDriverManager().install()))
    elif browser == "chrome":
        driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
    elif browser == "safari":
        safari_options = SafariOptions()
        driver = webdriver.Safari(service = Service(executable_path='/usr/bin/safaridriver'), options=safari_options)

    driver.maximize_window()
    request.cls.driver = driver
    logger.info("Webdriver initialization finished.")
    
    yield driver

    logger.info("Closing Webdriver instance.")
    driver.quit()


#this will get the value of CLI/Hooks
def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url")


#This will return the browser value to setup method
@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


#This will return the url value to setup method
@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")