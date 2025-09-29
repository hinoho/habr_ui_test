from library.pages.base_page import BasePage


class CompanyInfoPage(BasePage):
    page_element = '[action="/ru/companyinfo/"]'

    @staticmethod
    def open(page):
        page.goto()
        return CompanyInfoPage(page)