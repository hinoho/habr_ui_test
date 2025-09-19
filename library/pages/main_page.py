from library.pages.base_page import BasePage


class MainPage(BasePage):
    page_element = '.my-feed-page'

    @staticmethod
    def open(page):
        page.goto('https://habr.com/')
        return MainPage(page)

    def click_open_articles_page(self):
        self.click('a[href="/ru/articles/"]')
        from library.pages.articles_page import ArticlesPage
        return ArticlesPage(self.page).check_page()

    def click_open_search_page(self):
        self.click('a[href="/ru/search/"]')
        from library.pages.search_page import SearchPage
        return SearchPage(self.page).check_page()

