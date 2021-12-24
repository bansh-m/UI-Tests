import selenium
from main_page import main_page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginSearchLocators:
    ROZKLAD_SEARCH_SELECTOR_ID = (By.ID, "ctl00_MainContent_ctl00_txtboxGroup")
    ROZKLAD_RESULT_SELECTOR_ID = (By.ID, "ctl00_MainContent_lblHeader")

    ROZKLAD_SESSION_SELECTOR_ID = (By.CSS_SELECTOR, '[class="btn btn-link"]')
    ROZKLAD_SESSION_RESULT_ID = (By.CSS_SELECTOR, '[class="plainLink"]')

class SearchHelper(main_page):

    def go_to_session(self):
        search_field = self.find_element(LoginSearchLocators.ROZKLAD_SESSION_SELECTOR_ID)
        search_field.click()
        return search_field

    def enter_group(self, word):
        search_field = self.find_element(LoginSearchLocators.ROZKLAD_SEARCH_SELECTOR_ID)
        search_field.click()
        search_field.send_keys(word)
        search_field.send_keys(Keys.RETURN)
        return search_field
    
    def read_response(self):
        return self.find_element(LoginSearchLocators.ROZKLAD_RESULT_SELECTOR_ID).text

    def read_session_response(self):
        return self.find_element(LoginSearchLocators.ROZKLAD_SESSION_RESULT_ID).text
