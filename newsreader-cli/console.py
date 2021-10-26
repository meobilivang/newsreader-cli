import os
import scraper
from constants import constants

class Console:
    def __init__(self) -> None:
        pass

    def start_program():
        print(
            """
            #########################################################

                            WELCOME TO NEWSREADER-CLI
            
            #########################################################
            """
        )

    def display_options_mainscreen_start():
        print(
            """
            Choose the following options:
                a. Visit main board 
                b. Show Categories 
            """
        )

    def display_options_mainscreen_end():
        print(
            """
            Choose the following options:
                a. Refresh main board 
                b. Show Categories
                c. Read a specific news
            """
        )

    def display_main_page(article_list):
        print(
            """

            """
        )

    def display_detail_article(article):
        pass

    def handler_mainscreen_start():
        pass

    def handler_mainscreen_end():
        pass

console = Console()
