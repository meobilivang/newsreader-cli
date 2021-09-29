import requests
from bs4 import BeautifulSoup

URL = 'https://vnexpress.net/'

page = requests.get(URL).text

soup = BeautifulSoup(page, "html.parser")

article_list_raw = soup.find_all('article')

for article_raw in article_list_raw:
    headline = article_raw.h3.get_text().strip()
    url = article
    desc = "" if article_raw.p.get_text() is None else article_raw.p.get_text().strip()
    print(headline)
    print(desc)
    print('----------')



