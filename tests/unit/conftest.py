import pytest
import utils.globals as globals


from utils.logger import logger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import Options as SafariOptions


@pytest.fixture(scope='class')
def setup(request, browser):
    logger.step("Prepare instance of Webdriver")

    if browser == "edge":
        options = EdgeOptions()
        driver = webdriver.Remote(
            command_executor = globals.SEL_GRID_URL,
            options = options)

    elif browser == "chrome":
        options = ChromeOptions()
        driver = webdriver.Remote(
            command_executor = globals.SEL_GRID_URL,
            options = options)
            
    elif browser == "safari":
        options = SafariOptions()
        driver = webdriver.Safari(service = Service(
            executable_path = globals.SAFARI_DRIVER_PATH),
            options = options)

    driver.maximize_window()
    request.cls.driver = driver
    
    yield driver

    logger.step("Closing instance of Webdriver.")
    driver.quit()


@pytest.fixture(scope='function', autouse=True)
def test_log(request):
    logger.info(f"Starting Test Case: {request.node.name.upper()}")

    def fin():
        logger.info(f"Completed Test Case: {request.node.name.upper()}")

    request.addfinalizer(fin)


# This will get the value of CLI/Hooks
def pytest_addoption(parser):
    parser.addoption("--browser", default="edge") 


# This will return the browser value to setup method
@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")
