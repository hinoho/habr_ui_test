from library.pages.base_page import BasePage


class UserInfoPage(BasePage):
    page_element = 'user_info'

    @staticmethod
    def open(page):
        page.goto()
        return UserInfoPage(page)