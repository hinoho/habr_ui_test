from library.pages.base_page import BasePage


class HubsPage(BasePage):
    page_element = '.tm-hubs-list'

    @staticmethod
    def open(page):
        page.goto('https://habr.com/ru/articles/')
        return HubsPage(page)