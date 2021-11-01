import pytest

from newsreadercli import NewsScraper
from newsreadercli import Article

def test_web_scraper():
    
    scraper = NewsScraper()

    test_page = open("tests/test_data/vnexpress-test.html", 'r', encoding='utf-8')
    scraper.page_scrape(None, test_page.read())
    
    for article in scraper.articles_current_page:
        assert isinstance(article) is Article

    for category in scraper.categories:
        assert type(category) is str
