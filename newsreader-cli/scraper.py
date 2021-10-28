import requests
import time
from typing import List
from article import Article
from constants import constants
from utility import text_convert
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

class NewsScraper:
    
    def __init__(self, categories = {}, articles_current_page = []):
        self.categories = categories
        self.articles_current_page = articles_current_page
    
    @categories.getter
    def categories(self):
        return self.categories
    
    @categories.setter
    def categories(self, input_categories):
        self.categories = input_categories
    
    @articles_current_page.getter
    def articles_current_page(self):
        return self.articles_current_page
    
    @articles_current_page.setter
    def articles_current_page(self, articles):
        self.articles_current_page = articles
    
    def clear_articles(self):
        """
            Clear articles list
        """
        del self.articles [:]
    
    def default(self):
        self.page_scrape()                                  # Default values

    def make_soup(self, url: str = None) -> BeautifulSoup:
        try:
            page = requests.get(constants.BASE_URL if (url is None) else url).text
            time.sleep(0.1)
        except (URLError, HTTPError) as error:
            return None

        return BeautifulSoup(page, "html.parser")

    def page_scrape(self, url = None) -> List[Article]:
        soup = self.make_soup(url)
        
        # `categories` is empty
        if not self.categories:
            self.main_page_category(soup)

        article_list_raw = soup.find_all('article')    
        article_list = []

        for article_raw in article_list_raw:
            article_basics = article_raw.find('a')
            if article_basics is not None:
                article_list.append(Article(
                    article_basics.text,                    # Title
                    article_basics.get('href'),             # URL
                    text_convert(article_raw.p)             # Description
                ))
        #TODO: Debug
        self.articles_ = article_list
        #print(self.__get_articles__())

    def main_page_category(self, soup):
        category_dict = {}

        for category_raw in soup.find_all('li', { "data-id": True }):
            inner_tag = category_raw.find("a")

            category_url = inner_tag.get('href').replace('/', '')
            category_title = inner_tag.text.replace('\n', '').replace('\r', '').strip()
            
            if category_title.lower() != constants.NOT_SUPPORTED_FORMAT: 
                category_dict[category_title] = "{}{}".format(constants.BASE_URL, category_url)

        self.__set_categories__(category_dict)        

    def article_scrape(self, article: Article) -> Article:
        soup = self.make_soup(article.__get_url__())

        article_date_raw = soup.find("span", class_="date")
        article_category_list_raw = soup.find("ul", class_="breadcrumb").find_all("a")
        article_text_content_list_raw = soup.find_all('p', class_="Normal")

        article_date = text_convert(article_date_raw)
        article_category_list = [elem.text for elem in article_category_list_raw]
        content_paragraphs = [text_convert(article) for article in article_text_content_list_raw]

        article.__set_date__(article_date)
        article.__set_category__(article_category_list)
        article.__set_text_content__(content_paragraphs)