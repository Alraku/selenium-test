import os
import pytest
import logging

from datetime import datetime
from tests.unit._webdriver import WebDriver

start_time = datetime.strftime(datetime.now(), '%Y-%m-%d__%H-%M-%S')


@pytest.hookimpl
def pytest_runtest_setup(item):
    logging_plugin = item.config.pluginmanager.get_plugin("logging-plugin")
    logging_plugin.set_log_path(
        os.path.join('logs', f'test_session_{start_time}', f'{item.name}.log'))


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope='session', autouse=True)
def logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    return logger


@pytest.fixture(autouse=True)
def logger_result(request, logger):
    test_case_name = request.node.name.upper()
    logger.info(f"Execution of Test Case: {test_case_name} has started.")

    def fin():
        logger.info(f"Execution of Test Case: {test_case_name} has ended.")
        if request.node.rep_call.passed:
            logger.info("RESULT: PASSED")
        else:
            logger.info("RESULT: FAILED")

    request.addfinalizer(fin)


def pytest_addoption(parser):
    parser.addoption("--browser", default="safari")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope='class')
def setup(request, browser, logger):
    logger.info("Preparing instance of Webdriver")
    driver = WebDriver().get_webdriver(browser)

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    logger.info("Closing instance of Webdriver.")
    driver.quit()
