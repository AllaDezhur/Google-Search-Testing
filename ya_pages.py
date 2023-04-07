from selenium.webdriver.common.by import By

from base_page import BasePage

class YaSearchLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.CSS_SELECTOR, "input[name = 'q']")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.XPATH, "//form/div[1]/div[1]/div[4]//input[1]")

class SearchHelper(BasePage):
    def enter_word(self,word):
        search_field = self.find_element(YaSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field
    def click_on_search_button(self):
        return self.find_element(YaSearchLocators.LOCATOR_YANDEX_SEARCH_BUTTON).submit()
