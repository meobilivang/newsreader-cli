import requests

from bs4 import BeautifulSoup
from article import Article

def text_convert(input):
    """
        input: raw scraped html
    """
    return "" if input is None else input.get_text().strip()

BASE_URL = 'https://vnexpress.net/'
page = requests.get(BASE_URL).text

soup = BeautifulSoup(page, "html.parser")

article_list_raw = soup.find_all('article')
article_list = []
counter = 0

for article_raw in article_list_raw:
    
    article_list.append(Article(
        text_convert(article_raw.h3.a), 
        article_raw.h3.a['href'], 
        text_convert(article_raw.p)
    ))
    
    counter += 1

    #print(counter)
    # print(article_list.__get_title__())
    # print(article_list.__get_url__())
    # print(article_list.__get_description__())
    #print('----------')

def make_soup(url = None):
    page = requests.get(BASE_URL if url is None else url).text
    return BeautifulSoup(page, "html.parser")

def article_scrape(article):
    soup = make_soup(article.__get_url__())
    
    # article_header = soup.find_all("div", class_="header_conent") 
    
    # for tag in article_header:
    #     article_date = tag.find_all("span", class_="date")
    #     print(type(article_date))
    #     article_category_list = tag.find_all("li")
    #     print(article_category_list)

    #for each_category in article_category_list:
        #article.__insert_category(each_category)

    article_text_content_list_raw = soup.find_all('p', class_="Normal")
    #print(article_text_content_list_raw)
    for tag in article_text_content_list_raw:
        print(tag)

    # for each_paragraph in article_text_content_list:
    #     article.__insert_text_content(each_paragraph)
    #     print(article_text_content_list)

    return

print(article_list[0].url)
article_scrape(article_list[0])

