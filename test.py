from ya_pages import SearchHelper
from search_page import SearchPageHelper
#import allure


def test_search(browser):
    ya_main_page = SearchHelper(browser)
    ya_search_page = SearchPageHelper(browser)
    ya_main_page.go_to_site()
    ya_main_page.enter_word("Privet")
    ya_main_page.click_on_search_button()
    elements = ya_search_page.check_navi_bar()


    #for i in range(len(elements)):
    assert "Картинки" != ''.join(elements)

         #assert elements[i] != "Картинки"
    print("Такая кнопка есть")
    print(''.join(elements))