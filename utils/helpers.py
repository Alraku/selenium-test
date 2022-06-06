import os
import json

from datetime import datetime


cookie_path = "/../utils/cookies/cookies.pkl"

class CookieOperations:


    @staticmethod
    def save_cookie(driver):
        with open(os.path.dirname(__file__) + cookie_path, 'w') as filehandler:
            json.dump(driver.get_cookies(), filehandler)


    @staticmethod
    def load_cookie(driver):
        with open(os.path.dirname(__file__) + cookie_path, 'r') as cookiefile:
            cookies = json.load(cookiefile)
        for cookie in cookies:
            cookie.pop('domain', None)
            driver.add_cookie(cookie)


def get_time() -> str:
    return datetime.now().strftime("%Y-%m-%d__%H:%M:%S")