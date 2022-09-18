from pages._base import BasePage
from pages._locators import PageResultsLocators as Locator


class PageResults(BasePage):

    def __init__(self, driver) -> None:
        super().__init__(driver, '')

    def has_element_reloaded(self):
        skeleton_wrapper = self.find_element(Locator.RESULTS_SKELETON_WRAPPER)
        self.wait(3)
        return True if skeleton_wrapper is not None else False

    def extract_number_from_str(self):
        return int(
            "".join(filter(
                str.isdigit,
                self.find_element(Locator.NUMBER_OF_ADS_FOUND)).text))

    def click_checkbox(self, checkbox):
        if checkbox == 'description':
            self.find_element(Locator.CHECKBOX_DESCRIPTION).click()
        elif checkbox == 'photos':
            self.find_element(Locator.CHECKBOX_PHOTOS).click()
        elif checkbox == 'delivery':
            self.find_element(Locator.CHECKBOX_DELIVERY).click()

    def check_result(self, result) -> bool:
        self.logger.info("Verifying page results webtitle.")
        expected = result
        actual = self.get_title()

        if actual == expected:
            self.logger.info("Proper webtitle detected.")
            return True
        else:
            self.logger.error(
                f"Assertion Failed, expected: {expected}, actual: {actual}")
            return False