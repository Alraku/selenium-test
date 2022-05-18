from lib2to3.pgen2 import driver
from subprocess import TimeoutExpired
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PageLogin():

    textfield_username = "userEmail"
    textfield_password = "userPass"
    sign_in_button = 'se_userLogin'
    privacy_dialog_button = "onetrust-accept-btn-handler"


    def __init__(self, driver):
        self.driver = driver

    
    def enter_credentials(self, username, password):
        try:
            element_present = EC.presence_of_element_located((By.ID, self.sign_in_button))
            WebDriverWait(driver, 10).until(element_present)
        except TimeoutError:
            print("Element Not Found")

        self.driver.find_element(By.ID, self.textfield_username).clear()
        self.driver.find_element(By.ID, self.textfield_username).send_keys(username)
        self.driver.find_element(By.ID, self.textfield_password).send_keys(password)


    def click_login_button(self):
        self.driver.find_element(By.ID, self.sign_in_button).click()


    def accept_privacy_dialog(self):
        self.driver.find_element(By.ID, self.privacy_dialog_button).click()