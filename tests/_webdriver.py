import time
import logging
import json
import os

from utils.globals import SEL_GRID_URL, SAFARI_DRIVER_PATH
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

cookie_path = os.path.dirname(__file__) + "/cookies"
logger = logging.getLogger(__name__)


class WebDriver(object):

    def __init__(self) -> None:
        self.driver = None

    def get_webdriver(self, browser) -> webdriver:
        if browser == "edge":
            driver = webdriver.Remote(
                command_executor=SEL_GRID_URL,
                options=EdgeOptions())

        elif browser == "chrome":
            driver = webdriver.Remote(
                command_executor=SEL_GRID_URL,
                options=ChromeOptions())

        elif browser == "safari":
            driver = webdriver.Safari(service=Service(
                executable_path=SAFARI_DRIVER_PATH),
                options=SafariOptions())

        driver.maximize_window()
        self.driver = driver
        return self.driver

    @staticmethod
    def save_cookie(driver) -> None:
        logger.info("Saving cookies to pickle file.")
        if not os.path.exists(cookie_path):
            os.makedirs(cookie_path)
        with open(cookie_path + '/cookies.pkl', 'w') as filehandler:
            json.dump(driver.get_cookies(), filehandler)

    @staticmethod
    def load_cookie(driver) -> None:
        logger.info("Loading cookies from pickle file.")
        with open(cookie_path + '/cookies.pkl', 'r') as cookiefile:
            cookies = json.load(cookiefile)
        for cookie in cookies:
            cookie.pop('domain', None)
            driver.add_cookie(cookie)
        time.sleep(3)

    def clear_cookie(self) -> None:
        self.driver.delete_all_cookies()

    def delete_cache(self) -> None:
        self.driver.execute_script("window.open('')")  # Create a separate tab than the main one
        self.driver.switch_to.window(self.driver.window_handles[-1])  # Switch window to the second tab
        self.driver.get('chrome://settings/clearBrowserData')  # Open your chrome settings.
        self.perform_actions(Keys.TAB * 2 + Keys.DOWN * 4 + Keys.TAB * 5 + Keys.ENTER)  # Tab to the time select and key down to say "All Time" then go to the Confirm button and press Enter
        self.driver.close()  # Close that window
        self.driver.switch_to.window(self.driver.window_handles[0])  # Switch Selenium controls to the original tab to continue normal functionality.

    def perform_actions(self, keys):
        actions = ActionChains(self.driver)
        actions.send_keys(keys)
        self.wait(2)
        print('Performing Actions!')
        actions.perform()

    def close_all(self) -> None:
        if len(self.driver.window_handles) < 1:
            return
        for window_handle in self.driver.window_handles[:]:
            self.driver.switch_to.window(window_handle)
            self.driver.close()
