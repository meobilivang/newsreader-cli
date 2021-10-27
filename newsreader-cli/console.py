import os
from typing import Dict, List
import scraper
from constants import constants
from article import Article


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
    
    def end_program():
        print(
            """
            #########################################################

                                        BYE BYE
            
            #########################################################
            """
        )
    
    def display_list_option(arg: List):
        print("Choose the following options:")
        for index, elem in enumerate(arg):
            "({})\t{}".format(index, elem)
    
    def display_options_menu(self):
        self.display_options(constants.OPTIONS_MENU)

    def display_options_page(self):
        self.display_options(constants.OPTIONS_PAGE)
        
    # def display_options_category_page(self):
    #     self.display_options(constants.OPTIONS_ARTICLE)
    
    def display_options_article(self):
        self.display_options(constants.OPTIONS_ARTICLE)

    def display_page(self, category, article_list):
        print(category.center(50, '#'))
        
        for (index, article) in enumerate(article_list):
            print(''.center(40, '#'))
            print(constants.SECTION_MID_DELIMETER)
            print('{}. \t \t \t {}'.format(index, article.__get_title__()))
            print('"\x1B[3m{}\x1B[0m"'.format(article.__get_description__()))       # italics
            print(''.center(40, '#'))

    def display_detail_article(self, article):
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
    
    def display_categories(self, categories: Dict):
        self.display_list_option(list(categories.keys()))

    def handler_menu(self, user_input, scraper):
        if (user_input == '0'):             # Main page
            self.display_page(scraper.__get_articles__())
            
            page_execution = 0 
            while page_execution <= 0:
                self.display_options_page() 
                user_input = input(constants.PROMPT_INPUT)
                page_execution = self.handler_page(user_input, scraper.__get_articles__())

            return 0                        # Returns to Menu
        elif (user_input == '1'):           # Show categories
            self.display_categories(scraper.__get_categories())

            category_execution = 0 
            while category_execution <= 0:
                category_user_input = input(constants.PROMPT_INPUT)

                category_execution = self.handler_page(user_input, scraper.__get_articles__())

            return 0                        # Returns to Menu
        elif (user_input == '2'):           # Exit
            # Terminate
            program_termination = True
            return 1, program_termination
        else:
            print(constants.PROMPT_RE_INPUT)
            return -1                       # Ask user to re-input

    def handler_page(self, user_input, article_list: List[Article]):
        if (user_input == '0'):             # Read specific article
            
            article_pick_execution = 0
            while article_pick_execution <= 0:
                article_pick_index = input("Choose an article to read:")
                if (int(article_pick_index) < 0 or int(article_pick_index) >= len(article_list)):     # Invalid index
                    print("Invalid article.")
                else:
                    article_pick_execution = 1
                
            #Article found, display it
            self.display_article(int(article_pick_index))
            
            article_execution = 0
            while article_execution <= 0:
                self.display_options_article()
                article_user_input = input(constants.PROMPT_INPUT)
                article_execution = self.handler_article(article_user_input)

            return 0
        elif (user_input == '1'):           # Return to Menu
            return 1
        # elif (user_input == '2'):         
        #     # TODO: refresh
        #     pass
        else:
            print(constants.PROMPT_RE_INPUT)
            return -1
    
    def handler_category(self, user_input):
        if (user_input == '0'):
            self.display_page(scraper.__get_articles__())
            return 1
        else:
            print(constants.PROMPT_RE_INPUT)
            return -1

    def handler_article(self, user_input):
        if (user_input == '1'):             # Returns to previous page
            return 1
        else:
            print(constants.PROMPT_RE_INPUT)
            return -1