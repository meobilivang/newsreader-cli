import requests
import time

from typing import List
from newsreadercli.article import Article
from newsreadercli.constants import constants
from newsreadercli.utility import text_convert, text_sanitizer
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

class NewsScraper:
    
    def __init__(self, categories = {}, articles_current_page = []):
        self._categories = categories
        self._articles_current_page = articles_current_page
    
    @property
    def categories(self):
        return self._categories
    
    @property
    def articles_current_page(self):
        return self._articles_current_page

    @categories.setter
    def categories(self, input_categories):
        self._categories = input_categories
    
    @articles_current_page.setter
    def articles_current_page(self, articles):
        self._articles_current_page = articles
    
    def clear_articles(self):
        """
            Clear articles list
        """
        del self._articles [:]
    
    def default(self):
        self.page_scrape()                                  # Default values

    def make_soup(self, url = None, page = None) -> BeautifulSoup:
        if page is None:
            try:
                page = requests.get(constants.BASE_URL if (url is None) else url).text
                time.sleep(0.1)
            except (URLError, HTTPError) as error:
                return None

        return BeautifulSoup(page, "html.parser")

    def page_scrape(self, url = None, page = None) -> List[Article]:
        soup = self.make_soup(url, page)
        
        # `categories` is empty
        if not self.categories:
            self.main_page_category(soup)

        article_list_raw = soup.find_all('article')    
        article_list = []

        for article_raw in article_list_raw:
            article_basics = article_raw.find('a')
            if article_basics is not None:
                article_list.append(Article(
                    text_sanitizer(article_basics.text),                    # Title
                    article_basics.get('href'),             # URL
                    text_convert(article_raw.p)             # Description
                ))
        
        self.articles = article_list

    def main_page_category(self, soup):
        category_dict = {}

        for category_raw in soup.find_all('li', { "data-id": True }):
            inner_tag = category_raw.find("a")

            category_url = inner_tag.get('href').replace('/', '')
            category_title = text_sanitizer(inner_tag.text)
            
            if category_title.lower() != constants.NOT_SUPPORTED_FORMAT: 
                category_dict[category_title] = "{}{}".format(constants.BASE_URL, category_url)

        self.categories = category_dict        

    def article_scrape(self, article: Article) -> Article:
        soup = self.make_soup(article.url)

        article_date_raw = soup.find("span", class_="date")
        article_category_list_raw = soup.find("ul", class_="breadcrumb").find_all("a")
        article_text_content_list_raw = soup.find_all('p', class_="Normal")

        article_date = text_convert(article_date_raw)
        article_category_list = [elem.text for elem in article_category_list_raw]
        content_paragraphs = [text_convert(article) for article in article_text_content_list_raw]

        article.date = article_date
        article.category = article_category_list
        article.text_content = content_paragraphs