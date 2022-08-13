import pytest
from tests._webdriver import WebDriver

pytest_plugins = ("tests._hooks", "tests._logger")


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
