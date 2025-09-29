from library.pages.base_page import BasePage


class PostsPage(BasePage):
    page_element = '.tm-post-snippet'

    @staticmethod
    def open(page):
        page.goto('https://habr.com/ru/articles/')
        return PostsPage(page)