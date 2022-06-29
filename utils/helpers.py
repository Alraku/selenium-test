import os
import json

from datetime import datetime


cookie_path = os.path.dirname(__file__) + "/cookies"

class CookieOperations:


    @staticmethod
    def save_cookie(driver) -> None:
        if not os.path.exists(cookie_path):
            os.makedirs(cookie_path)
        with open(cookie_path + '/cookies.pkl', 'w') as filehandler:
            json.dump(driver.get_cookies(), filehandler)


    @staticmethod
    def load_cookie(driver) -> None:
        with open(cookie_path + '/cookies.pkl', 'r') as cookiefile:
            cookies = json.load(cookiefile)
        for cookie in cookies:
            cookie.pop('domain', None)
            driver.add_cookie(cookie)


def get_time() -> str:
    return datetime.now().strftime("%Y-%m-%d__%H:%M:%S")