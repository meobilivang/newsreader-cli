from scraper import NewsScraper
from article import Article
from console import console

def main():
    news_scrapper = NewsScraper()

    article_list_obj = news_scrapper.page_scrape()

    for elem in article_list_obj:
        print(elem.__get_title__())

if __name__ == "__main__":
    main()