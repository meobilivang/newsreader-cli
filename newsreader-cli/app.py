from scraper import NewsScraper
from article import Article
from console import Console

# def main():
#     news_scrapper = NewsScraper()

#     article_list_obj = news_scrapper.page_scrape()

#     for elem in article_list_obj:
#         print(elem.__get_title__())

def main():
    console = Console()
    news_scrapper = NewsScraper()
    
    while True:
        console.start_program()
        console.display_options_menu()

        while True:
            user_input = input("Please choose an option:")
            console.handler_menu(user_input)
        pass
        

if __name__ == "__main__":
    main()