import requests

from bs4 import BeautifulSoup
from article import Article

def text_convert(input):
    """
        input: raw scraped html
    """
    return "" if input is None else input.get_text().strip()

URL = 'https://vnexpress.net/'
page = requests.get(URL).text

soup = BeautifulSoup(page, "html.parser")

article_list_raw = soup.find_all('article')
article_list = []

for article_raw in article_list_raw:
    article_list.append(Article(
        text_convert(article_raw.h3.a), 
        article_raw.h3.a['href'], 
        text_convert(article_raw.p)
        ))

    print(article_list[-1].__get_title__())
    print(article_list[-1].__get_url__())
    print(article_list[-1].__get_description__())
    print('----------')



