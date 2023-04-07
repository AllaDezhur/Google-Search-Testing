from selenium.webdriver.common.by import By
from base_page import BasePage

class YaSearchPageLocators:
   LOCATOR_YANDEX_NAVI_BAR = (By.CLASS_NAME, "hdtb-mitem")

class SearchPageHelper(BasePage):
    def check_navi_bar(self):
        all_list = self.find_elements(YaSearchPageLocators.LOCATOR_YANDEX_NAVI_BAR)

        return [x.text for x in all_list]

