from library.pages.base_page import BasePage


class NewsPage(BasePage):
    page_element = 'news'

    @staticmethod
    def open(page):
        page.goto('https://habr.com/ru/articles/')
        return NewsPage(page)