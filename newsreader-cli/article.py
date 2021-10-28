from typing import Text

class Article:
    def __init__(self, title = "", url = "", description = "", text_content = [], date = "", category = []):
        self.title = title
        self.url = url
        self.description = description
        self.text_content = text_content
        self.date = date
        self.category = category

    @title.getter
    def title(self):
        return self.title
    
    @url.getter
    def url(self):
        return self.url
    
    @description.getter
    def description(self):
        return self.description

    @text_content.getter
    def text_content(self):
        return self.text_content

    @date.getter
    def date(self):
        return self.date
    
    @category.getter
    def category(self):
        return self.category
    
    @date.setter
    def date(self, date):
        self.date = date
    
    @text_content.setter
    def text_content(self, new_text_content_list):
        self.text_content = new_text_content_list
    
    @category.setter
    def category(self, new_category_list):
        self.category = new_category_list
    
