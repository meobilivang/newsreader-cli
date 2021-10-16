from typing import Text


class Article:
    def __init__(self, title = "", url = "", description = "", text_content = [], date = "", category = []):
        self.title = title
        self.url = url
        self.description = description
        self.text_content = text_content
        self.date = date
        self.catergory = category

    def __get_title__(self):
        return self.title
    
    def __get_url__(self):
        return self.url
    
    def __get_description__(self):
        return self.description
    
    def __get_text_content__(self):
        return self.text_content

    def __get_date__(self):
        return self.date
    
    def __get_catergory__(self):
        return self.category
    
    def __set_date__(self, date):
        self.date = date
    
    def __set_text_content__(self, new_text_content_list):
        self.text_content = new_text_content_list
    
    def __set_category__(self, new_category_list):
        self.category = new_category_list
    
