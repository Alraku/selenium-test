import time
import logging

from utils.globals import BASE_URL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver, url_path: str):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.url_path = BASE_URL + url_path


    def open(self):
        self.driver.get(self.url_path)


    def find_element(self, locator: tuple[By, str], timeout: int = 3) -> WebElement:
        (locator_type, locator_value) = locator
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((
                    locator_type, locator_value)))
            return element

        except TimeoutException as Exception:
            self.logger.warning("Element not found in desired time.")
            raise Exception


    def page_scroll(self, height) -> None:
        self.logger.info(f"Scrolling page to Y: {height}")
        self.driver.execute_script(f"window.scrollTo(0, {height})")


    def wait(self, timeout) -> None:
        self.logger.info(f"Waiting: {timeout} seconds.")
        time.sleep(timeout)