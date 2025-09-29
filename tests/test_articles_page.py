#разные взаимодействия
def test_open_posts_page(open_article_page_fixture):
    open_article_page_fixture.click_open_posts_page()

def test_open_news_page(open_article_page_fixture):
    open_article_page_fixture.click_open_news_page()

def test_open_users_page(open_article_page_fixture):
    open_article_page_fixture.click_open_users_page()

def test_open_hubs_page(open_article_page_fixture):
    open_article_page_fixture.click_open_hubs_page()

def test_open_companies_page(open_article_page_fixture):
    open_article_page_fixture.click_open_companies_page()

def test_sort_articles(open_article_page_fixture):
    pass
