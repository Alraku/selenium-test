#from lib2to3.pgen2 import driver
import time
import json 

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PageLogin():

    textfield_username = "userEmail"
    textfield_password = "userPass"
    sign_in_button = 'se_userLogin'
    privacy_dialog_button = "onetrust-accept-btn-handler"

    cookie_path = "/Users/alraku/Documents/Visual Studio Code/Projects/Test-Automation/utils/cookies/cookies.pkl"


    def __init__(self, driver):
        self.driver = driver

    
    def enter_credentials(self, username, password):
        try:
            element_present = EC.presence_of_element_located((By.ID, self.sign_in_button))
            WebDriverWait(self.driver, 10).until(element_present)
        except:
            print("Element Not Found")

        self.driver.find_element(By.ID, self.textfield_username).clear()
        self.driver.find_element(By.ID, self.textfield_username).send_keys(username)
        self.driver.find_element(By.ID, self.textfield_password).send_keys(password)


    def click_login_button(self, timeout):
        self.driver.find_element(By.ID, self.sign_in_button).click()
        time.sleep(timeout)


    def accept_privacy_dialog(self):
        self.driver.find_element(By.ID, self.privacy_dialog_button).click()


    def save_cookie(self):
        with open(self.cookie_path, 'w') as filehandler:
            json.dump(self.driver.get_cookies(), filehandler)


    def load_cookie(self):
        with open(self.cookie_path, 'r') as cookiefile:
            cookies = json.load(cookiefile)
        for cookie in cookies:
            self.driver.add_cookie(cookie)