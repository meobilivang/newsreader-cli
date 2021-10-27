from scraper import NewsScraper
from article import Article
from console import Console
from constants import constants

# def main():
#     news_scrapper = NewsScraper()

#     article_list_obj = news_scrapper.page_scrape()

#     for elem in article_list_obj:
#         print(elem.__get_title__())

def main():
    run_program = True
    console = Console()
    news_scrapper = NewsScraper()
    news_scrapper.default()
    
    print(news_scrapper.__get_articles__())
    
    # console.start_program()

    # while run_program:
    #     #console.display_options_menu()

    #     menu_execution = 0
    #     while menu_execution <= 0:
    #         #TODO: remove
    #         #time.sleep(0.1)
    #         console.display_options_menu()
    #         user_input = input(constants.PROMPT_INPUT)
    #         menu_execution, program_termination = console.handler_menu(user_input, news_scrapper)
    #         run_program = True if program_termination is None else False           # Exit program

    # console.end_program()    

if __name__ == "__main__":
    main()