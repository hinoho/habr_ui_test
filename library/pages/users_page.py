from library.pages.base_page import BasePage


class UsersPage(BasePage):
    page_element = '.tm-users-list'

    @staticmethod
    def open(page):
        page.goto('https://habr.com/ru/articles/')
        return UsersPage(page)