from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    """A class for login page locators. All login page locators should come here"""

    INPUT_USERNAME = (By.XPATH, '//*[@id="userEmail"]')
    INPUT_PASSWORD = (By.XPATH, '//*[@id="userPass"]')
    BUTTON_SIGN_IN = (By.XPATH, '//*[@id="se_userLogin"]')
    BUTTON_PRIVACY_ACCEPT = (By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
    LABEL_INVALID_CREDS = (By.XPATH, '//label[@for="userPass" and @class="error"]')

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""

    NUMBER_OF_ADS_FOUND = (By.CSS_SELECTOR, 'div[data-testid="total-count"]')
    RESULTS_SKELETON_WRAPPER = (By.CSS_SELECTOR, 'ul[data-testid="qa-skeleton-wrapper"]')
    CHECKBOX_NAME = ()

class AddAdvertPageLocators(object):
    """A class for add advert locators. All add advert locators should come here"""

    INPUT_TITLE = (By.XPATH, '//textarea[@data-cy="posting-title"]')
    BUTTON_CATEGORY = (By.XPATH, '//div[@data-cy="posting-select-category"]')
    BUTTON_SUGGESTED_CATEGORY = (By.XPATH, '//button[@data-cy="posting-suggested-categories-item"]')
    INPUT_DESCRIPTION = (By.XPATH, '//textarea[@name="description"]')
    INPUT_PHOTOS = (By.ID, "photo-attachment-files")
    INPUT_PRICE = (By.ID, 'parameters.price.price')
    BUTTON_FREE = (By.XPATH, '//button[text()="Za darmo"]')
    BUTTON_EXCHANGE = (By.XPATH, '//button[text()="Zamienię"]')
    BUTTON_TYPE_PRIVATE = (By.XPATH, '//button[text()="Prywatne"]')
    BUTTON_TYPE_BUSINESS = (By.XPATH, '//button[text()="Firmowe"]')
    BUTTON_ITEM_CONDITION = (By.XPATH, '//button[@placeholder="Wybierz"]')
    INPUT_LOCATION = (By.XPATH, '//input[@data-cy="location-search-input"]')
    BUTTON_DELIVERY = (By.XPATH, '//h6[text()="Dodaj Przesyłkę OLX"]')
    BUTTON_SUBMIT = (By.XPATH, '//button[@type="submit"]')
    dialog1 = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div[2]/button')
    dialog2 = (By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div/footer/button/span/span')
    advert_title = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div/div[2]/div/div[1]/div[2]/div[1]/h5/a')
    suggested_location = (By.XPATH, '//*[@id="posting-form"]/main/div[1]/div[7]/div[2]/div/div/div/div/div/div/div[2]/li')