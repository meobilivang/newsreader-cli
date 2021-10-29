import pytest

from newsreadercli.scraper import NewsScraper
from newsreadercli.article import Article

def test_web_scraper():
    
    scraper = NewsScraper()

    test_page = open("tests/vnexpress-test.html", 'r', encoding='utf-8')
    scraper.page_scrape(None,  test_page.read())
    
    for article in scraper.articles_current_page:
        assert isinstance(article) is Article

    for category in scraper.categories:
        assert type(category) is str
