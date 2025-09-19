import pytest

from library.pages.articles_page import ArticlesPage
from library.pages.main_page import MainPage


@pytest.fixture
def open_main_page_fixture(habr_page_fixture):
    return MainPage.open(habr_page_fixture)

@pytest.fixture
def open_article_page_fixture(habr_page_fixture):
    return ArticlesPage.open(habr_page_fixture)


@pytest.fixture
def habr_page_fixture(browser):
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"

    context = browser.new_context(viewport={ 'width': 1280, 'height': 1024 },
                                  user_agent=ua,
                                  extra_http_headers={
                                      "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                                      'accept-language': "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6",
                                      'referer': 'https://habr.com/ru/search/'
            })
    page = context.new_page()
    yield page
    context.close()

