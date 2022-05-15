from selenium.webdriver.common.by import By


class PageLogin():

    textfield_username = "username"
    textfield_password = "password"
    login_button_xpath = "btn btn-action btn-lg btn-block loginbtn"


    def __init__(self, driver):
        self.driver = driver

    
    def enter_user_name(self, username):
        self.driver.find_element(By.NAME, self.textfield_username).send_keys(username)
