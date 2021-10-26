from typing import List
import requests
import time
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
from article import Article

BASE_URL = 'https://vnexpress.net/'
NOT_SUPPORTED_FORMAT = "video"

def text_convert(input) -> str:
    """
        input: raw scraped html
    """
    return "" if input is None else input.get_text().strip()

class NewsScraper:
    def __init__(self, categories = {}, articles_current_page = []):
        self.categories = categories
        self.articles_current_page = articles_current_page
    
    def __get_categories__():
        return self.categories
    
    def __set_categories__(input_categories):
        self.categories = input_categories
    
    def __get_articles__():
        return self.articles_current_page
    
    def __set_articles__(articles):
        self.articles = articles

def make_soup(url: str = None) -> BeautifulSoup:
    try:
        page = requests.get(BASE_URL if (url is None) else url).text
        time.sleep(0.1)
    except (URLError, HTTPError) as error:
        return None

    return BeautifulSoup(page, "html.parser")

def page_scrape(url = None) -> List[Article]:
    soup = make_soup(url)

    #TODO: Call main_page_category in the run of the program
    #if not __get_categories__():
        #main_page_category(soup)
    
    #TODO: Remove
    #print(main_page_category(soup))

    article_list_raw = soup.find_all('article')    
    article_list = []

    for article_raw in article_list_raw:
        if article_raw.find('a'):
            article_list.append(Article(
                text_convert(article_raw.h3.a),         # Title
                article_raw.h3.a['href'],               # URL
                text_convert(article_raw.p)             # Description
            ))
    
    #__set_articles__(article_list)
    
    return article_list

def main_page_category(soup):
    category_dict = {}

    for category_raw in soup.find_all('li', { "data-id": True }):
        inner_tag = category_raw.find("a")

        category_url = inner_tag.get('href').replace('/', '')
        category_title = inner_tag.text.replace('\n', '').replace('\r', '').strip()
        
        if category_title.lower() != NOT_SUPPORTED_FORMAT: 
            category_dict[category_title] = "{}{}".format(BASE_URL, category_url)

    # TODO: Set to property of NewsScraper
    return category_dict
    #__set_categories__(category_dict)

#TODO: Article obj is passed as arg
#def article_scrape(article: Article) -> Article:
def article_scrape(url) -> Article:
    #soup = make_soup(article.__get_url__())
    soup = make_soup(url)

    article_date_raw = soup.find("span", class_="date")
    article_category_list_raw = soup.find("ul", class_="breadcrumb").find_all("a")
    article_text_content_list_raw = soup.find_all('p', class_="Normal")

    article_date = text_convert(article_date_raw)
    article_category_list = [elem.text for elem in article_category_list_raw]
    content_paragraphs = [text_convert(article) for article in article_text_content_list_raw]

    #article.__set_date__(article_date)
    #article.__set_category__(article_category_list)
    #article.__set_text_content__(content_paragraphs)

    #return article
    
article_obj_list = page_scrape("https://vnexpress.net/the-gioi")

#print(article_list)

#article = article_scrape("https://vnexpress.net/hanh-khach-di-may-bay-tiep-tuc-khai-bao-thong-tin-4377088.html")
#print(article.__dict__)