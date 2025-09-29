from library.pages.base_page import BasePage


class SearchPage(BasePage):
    page_element = '[action="/ru/search/"]'

    @staticmethod
    def open(page):
        page.goto('https://habr.com/ru/articles/')
        return SearchPage(page)
