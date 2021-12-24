from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class main_page:
    def __init__(self, driver):
        self.base_url = "http://rozklad.kpi.ua/Schedules/ScheduleGroupSelection.aspx"
        self.driver = driver
        
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)