from typing import Dict, List
import scraper
from constants import constants

class Console:
    def init(self) -> None:
        pass

    def start_program(self):
        print(
            """
            #########################################################

                            WELCOME TO NEWSREADER-CLI
            
            #########################################################
            """
        )
    
    def end_program(self):
        print(
            """
            #########################################################

                                    THANK YOU!
            
            #########################################################
            """
        )
    
    def display_options(self, arg: List):
        print(constants.SECTION_SMALL_DELIMETER)
        for index, elem in enumerate(arg):
            print("({})\t{}".format(index, elem))
    
    def display_options_menu(self):
        self.display_options(constants.OPTIONS_MENU)

    def display_options_page(self):
        self.display_options(constants.OPTIONS_PAGE)
    
    def display_options_article(self):
        self.display_options(constants.OPTIONS_ARTICLE)

    def display_page(self, category, article_list):
        print(constants.SECTION_MED_DELIMETER)
        category = "Menu" if category is None else category

        print(category.center(50, '#'))
        
        for (index, article) in enumerate(article_list):
            print(constants.SECTION_SMALL_DELIMETER)
            print(''.center(80, '-'))
            print('{}. \t \t \t {}'.format(index, article.title))
            print('"{}"'.format(article.description))       # italics
            print(''.center(80, '-'))

    def display_article(self, article):
        print(constants.SECTION_MED_DELIMETER)
        print(article.title.center(70, '#'))
        print(constants.SECTION_SMALL_DELIMETER)
        
        display_category = ""
        for category in article.category:
            display_category += category + " >>> "

        print("{}\t \t \t \t{}".format(display_category, article.date)) 
        print(constants.SECTION_SMALL_DELIMETER)

        for paragraph in article.text_content:
            print('\t{}'.format(paragraph))
        
        print(''.center(40, '#'))
    
    def display_categories(self, categories: Dict):
        self.display_options(categories)

    def handler_menu(self, user_input, scraper):
        if (user_input == '0'):             # Main page
            page_execution = 0 
            
            while page_execution <= 0:
                self.display_page(None, scraper.articles)
                self.display_options_page() 
                user_input = input(constants.PROMPT_INPUT)
                page_execution = self.handler_page(user_input, scraper)

            return 0, None                        # Returns to Menu
        elif (user_input == '1'):                 # Show categories
            categories = scraper.categories
            categories_key_list = list(categories.keys())

            self.display_categories(categories_key_list)

            category_pick_execution = 0 
            while category_pick_execution <= 0:
                category_pick_user_input = int(input(constants.PROMPT_INPUT))
                if (category_pick_user_input < 0 \
                    or category_pick_user_input > len(categories_key_list)):     # Invalid index
                    print("Invalid Category.")
                else:
                    category_pick_execution = 1
            
            # Scrape Page by category
            scraper.page_scrape(categories.get(categories_key_list[category_pick_user_input]))

            category_page_execution = 0 
            while category_page_execution <= 0:
                self.display_page(categories_key_list[category_pick_user_input], scraper.articles)
                self.display_options_page() 
                user_input = input(constants.PROMPT_INPUT)
                category_page_execution = self.handler_page(user_input, scraper)

            return 0, None                        # Returns to Menu
        elif (user_input == '2'):           # Exit
            # Terminate
            program_termination = True
            return 1, program_termination
        else:
            print(constants.PROMPT_RE_INPUT)
            return -1, None                         # Ask user to re-input

    def handler_page(self, user_input, scraper):
        if (user_input == '0'):                     # Read specific article
            article_pick_execution = 0
            while article_pick_execution <= 0:
                article_pick_index = input("Choose an article to read: ")

                if (int(article_pick_index) < 0 or 
                        int(article_pick_index) > len(scraper.articles)):     # Invalid index
                    print("Invalid Article.")
                else:
                    article_pick_execution = 1
            
            article_list = scraper.articles

            scraper.article_scrape(
                article_list[int(article_pick_index)]
            )

            #Article found, display it
            self.display_article(
                article_list[int(article_pick_index)]
            )
            
            article_execution = 0
            while article_execution <= 0:
                self.display_options_article()
                article_user_input = input(constants.PROMPT_INPUT)
                article_execution = self.handler_article(article_user_input)

            return 0
        elif (user_input == '1'):           # Return to Menu
            return 1
        # TODO: refresh
        # elif (user_input == '2'):         
        #     pass
        else:
            #print(constants.PROMPT_RE_INPUT)
            return -1

    def handler_article(self, user_input):
        if (user_input == '0'):             # Returns to previous page
            return 1
        else:
            print(constants.PROMPT_RE_INPUT)
            return -1