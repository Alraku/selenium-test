#coding: utf-8
import pytest
import utils.globals as globals


from utils.logger import logger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import Options as SafariOptions


@pytest.fixture(scope='class')
def setup(request, browser, mode):
    if browser == "edge":
        options = EdgeOptions()
        # driver = webdriver.Edge(service = Service(EdgeChromiumDriverManager().install()))
        driver = webdriver.Remote(
            command_executor = globals.SEL_GRID_URL,
            options = options)

    elif browser == "chrome":
        options = ChromeOptions()
        # driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        driver = webdriver.Remote(
            command_executor = globals.SEL_GRID_URL,
            options = options)
            
    elif browser == "safari":
        safari_options = SafariOptions()
        driver = webdriver.Safari(service = Service(
            executable_path = globals.SAFARI_DRIVER_PATH),
            options = safari_options)

    driver.maximize_window()
    request.cls.driver = driver
    logger.info("Webdriver initialization finished.")
    
    yield driver

    logger.info("Closing Webdriver instance.")
    driver.quit()


# This will get the value of CLI/Hooks
def pytest_addoption(parser):
    # safari edge chrome
    parser.addoption("--browser", default="edge") 
    # local remote
    parser.addoption("--mode", default="local")


# This will return the browser value to setup method
@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


# This will return the mode value to setup method
@pytest.fixture(scope="class", autouse=True)
def mode(request):
    return request.config.getoption("--mode")