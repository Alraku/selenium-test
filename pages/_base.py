import imp
import logging
from utils.globals import BASE_URL


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver, url_path: str):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.url_path = BASE_URL + url_path


    def open(self):
        self.driver.get(self.url_path)