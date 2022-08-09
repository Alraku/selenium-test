from utils.globals import SEL_GRID_URL, SAFARI_DRIVER_PATH
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import Options as SafariOptions


class WebDriver(object):

    def __init__(self) -> None:
        pass

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
        return driver
