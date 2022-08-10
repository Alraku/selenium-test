import os
import json
import logging

from datetime import datetime

cookie_path = os.path.dirname(__file__) + "/cookies"
logger = logging.getLogger(__name__)


class CookieOperations(object):

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


def get_time() -> str:
    return datetime.now().strftime("%Y-%m-%d__%H:%M:%S")
