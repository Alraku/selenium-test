import os
import json


class CookieOperations:

    cookie_path = "/../utils/cookies/cookies.pkl"


    @classmethod
    def save_cookie(cls, driver):
        with open(os.path.dirname(__file__) + cls.cookie_path, 'w') as filehandler:
            json.dump(driver.get_cookies(), filehandler)


    @classmethod
    def load_cookie(cls, driver):
        with open(os.path.dirname(__file__) + cls.cookie_path, 'r') as cookiefile:
            cookies = json.load(cookiefile)
        for cookie in cookies:
            driver.add_cookie(cookie)