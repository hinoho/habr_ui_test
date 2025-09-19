from library.pages.base_page import BasePage


class ArticlesPage(BasePage):
    page_element = '.tm-article-snippet'

    @staticmethod
    def open(page):
        page.goto('https://habr.com/ru/articles/')
        return ArticlesPage(page)

    def click_open_posts_page(self):
        self.click('a[href="/ru/posts/"]')

        from library.pages.posts_page import PostsPage
        return PostsPage(self.page).check_page()

    def click_open_news_page(self):
        self.click('a[href="/ru/news/"]')

        from library.pages.news_page import NewsPage
        return NewsPage(self.page).check_page()

    def click_open_hubs_page(self):
        self.click('a[href="/ru/hubs/"]')
        from library.pages.hubs_page import HubsPage
        return HubsPage(self.page).check_page()

    def click_open_users_page(self):
        self.click('a[href="/ru/users/"]')
        from library.pages.users_page import UsersPage
        return UsersPage(self.page).check_page()

    def click_open_companies_page(self):
        self.click('a[href="/ru/companies/"]')
        from library.pages.companies_page import CompaniesPage
        return CompaniesPage(self.page).check_page()