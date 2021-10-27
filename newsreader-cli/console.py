import os
from typing import List
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
    
    def display_option_list(messages: List):
        print("Choose the following options:")
        for index, elem in enumerate(messages):
            "{}\t{}".format(index, elem)
        
    def display_options_menu():
        display_options(constants.OPTIONS_MENU)

    def display_options_page():
        display_options(constants.OPTIONS_PAGE)
        
    def display_options_category_page():
        display_options(constants.OPTIONS_ARTICLE)

    def display_page(category, article_list):
        print(category.center(50, '#'))
        
        for (index, article) in enumerate(article_list):
            print(''.center(40, '#'))
            print(constants.SECTION_MID_DELIMETER)
            print('{}. \t \t \t {}'.format(index, article.__get_title__()))
            print('"\x1B[3m{}\x1B[0m"'.format(article.__get_description__()))       # italics
            print(''.center(40, '#'))

    def display_detail_article(article):
        print(article.__get_title__().center(50, '#'))
        print(constants.SECTION_SMALL_DELIMETER)
        
        display_category = ""
        for category in article.__get_category__():
            display_category += category + ">>>"

        print("{}\t \t \t \t{}".format(display_category, article.__get_date__())) 
        print(constants.SECTION_SMALL_DELIMETER)

        for paragraph in article.__get_text_content__():
            print('\t\x1B[3m{}\x1B[0m'.format(paragraph))
        
        print(''.center(40, '#'))

    def handler_menu(user_input):
        if (user_input == '0'):
            pass
        elif (user_input == '1'):           # Show categories
            display_categories()
            pass
        elif (user_input == '2'):           # Exit
            pass
        else:
            pass
        pass

    def handler_page(user_input):
        pass
    
    def handler_article(user_input):
        pass