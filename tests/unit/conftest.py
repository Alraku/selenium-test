import os
import pytest
import logging
import datetime
import utils.globals as globals


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import Options as SafariOptions

logger = logging.getLogger(__name__)
start_time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d__%H-%M-%S')


@pytest.hookimpl
def pytest_runtest_setup(item):
    logging_plugin = item.config.pluginmanager.get_plugin("logging-plugin")
    logging_plugin.set_log_path(os.path.join('logs', f'test_session_{start_time}', f'{item.name}.log'))


@pytest.fixture(scope='function', autouse=True)
def test_log(request):
    logger.info(f"Execution of Test Case: {request.node.name.upper()} has started.")

    def fin():
        logger.info(f"Execution of Test Case: {request.node.name.upper()} has ended.")

    request.addfinalizer(fin)


@pytest.fixture(scope='class')
def setup(request, browser):
    logger.info("Preparing instance of Webdriver")

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

    logger.info("Closing instance of Webdriver.")
    driver.quit()


# This will get the value of CLI/Hooks
def pytest_addoption(parser):
    parser.addoption("--browser", default="safari") 


# This will return the browser value to setup method
@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")