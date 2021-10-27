from scraper import NewsScraper
from article import Article
from console import Console

# def main():
#     news_scrapper = NewsScraper()

#     article_list_obj = news_scrapper.page_scrape()

#     for elem in article_list_obj:
#         print(elem.__get_title__())

def main():
    run_program = True
    console = Console()
    news_scrapper = NewsScraper()
    
    console.start_program()

    while run_program:
        console.display_options_menu()

        menu_execution = 0
        while menu_execution <= 0:
            user_input = input("Please choose an option:")
            menu_execution, program_termination = console.handler_menu(user_input, news_scrapper)
            run_program = True if program_termination is None else False                            # Exit program
    

    console.end_program()    

if __name__ == "__main__":
    main()