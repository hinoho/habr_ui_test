from library.pages.base_page import BasePage


class CompaniesPage(BasePage):
    page_element = '.tm-companies'

    @staticmethod
    def open(page):
        page.goto('https://habr.com/ru/articles/')
        return CompaniesPage(page)