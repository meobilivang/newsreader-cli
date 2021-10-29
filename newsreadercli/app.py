from scraper import NewsScraper
from console import Console
from constants import constants

def main():
    run_program = True
    console = Console()
    news_scrapper = NewsScraper()

    news_scrapper.default()
    console.start_program()

    while run_program:
        menu_execution = 0
        while menu_execution <= 0:
            console.display_options_menu()
            user_input = input(constants.PROMPT_INPUT)
            menu_execution, program_termination = console.handler_menu(user_input, news_scrapper)
            run_program = True if program_termination is None else False           # Exit program

    console.end_program()
    return 1

if __name__ == "__main__":
    main()