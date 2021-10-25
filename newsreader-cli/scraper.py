from typing import List
import requests
import time
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
from article import Article

BASE_URL = 'https://vnexpress.net/'
NOT_SUPPORTED_FORMAT = "video"

class NewsScraper:
    def __init__(self, categories = {}):
        self.categories = categories
    
    def __get_categories__():
        return self.categories
    
    def __set_categories_(input_categories):
        self.categories = input_categories
        

def make_soup(url: str = None) -> BeautifulSoup:
    try:
        page = requests.get(BASE_URL if url is None else url).text
        time.sleep(0.1)
    except (URLError, HTTPError) as error:
        return None

    return BeautifulSoup(page, "html.parser")

def text_convert(input) -> str:
    """
        input: raw scraped html
    """
    return "" if input is None else input.get_text().strip()

def page_scrape(url = "") -> List[Article]:
    soup = make_soup(url)

    article_list_raw = soup.find_all('article')    
    article_list = []

    for article_raw in article_list_raw:
        article_list.append(Article(
            text_convert(article_raw.h3.a), 
            article_raw.h3.a['href'], 
            text_convert(article_raw.p)
        ))

    return article_list

def main_page_category():
    soup = make_soup()
    
    category_dict = {}

    for category_raw in soup.find_all('li', { "data-id": True }):
        inner_tag = category_raw.find("a")

        category_url = inner_tag.get('href')
        category_title = inner_tag.text.replace('\n', '').replace('\r', '')
        
        if category_title.lower() != NOT_SUPPORTED_FORMAT: 
            category_dict[category_title] = category_url

    #__set_categories__(category_dict)
    # for x, (key, val) in enumerate(category_dict.items()):
    #     print(x, key, val)
    # TODO: Remove
    return category_dict


def article_scrape(article: Article) -> Article:
    soup = make_soup(article.__get_url__())

    if soup != None:
        article_date_raw = soup.find("span", class_="date")
        #article_header_raw = soup.find_all("div", class_="header_content") 
        #article_category_list_raw = soup.find_all("ul", class_="breadcrumb")
        article_text_content_list_raw = soup.find_all('p', class_="Normal")

        #print(article_category_list_raw)

        article_date = text_convert(article_date_raw)

        #article_category_list = [text_convert(category) for category in article_category_list_raw] 
        content_paragraphs = [text_convert(article) for article in article_text_content_list_raw]
        
        article.__set_date__(article_date)
        #article.__set_header__(article_header_raw)
        #article.__set_category__(article_category_list)
        article.__set_text_content__(content_paragraphs)
    print(article.__dict__)
    return article

article_list = main_page_category()
