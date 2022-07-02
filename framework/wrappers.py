import logging

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


logger = logging.getLogger(__name__)


def find_element(driver, locator: tuple[By, str], timeout: int = 3) -> WebElement:
    (locator_type, locator_value) = locator
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((
                locator_type, locator_value)))
        return element

    except TimeoutException as Exception:
        logger.warning("Element not found in desired time.")
        raise Exception


def page_scroll(driver, height) -> None:
    logger.info(f"Scrolling page to Y: {height}")
    driver.execute_script(f"window.scrollTo(0, {height})")