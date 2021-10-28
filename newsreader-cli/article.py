from typing import Text

class Article:
    def __init__(self, title = "", url = "", description = "", text_content = [], date = "", category = []):
        self._title = title
        self._url = url
        self._description = description
        self._text_content = text_content
        self._date = date
        self._category = category

    @property
    def title(self):
        return self._title
    
    @property
    def url(self):
        return self._url
    
    @property
    def description(self):
        return self._description

    @property
    def text_content(self):
        return self._text_content

    @property
    def date(self):
        return self._date
    
    @property
    def category(self):
        return self._category
    
    @date.setter
    def date(self, date):
        self._date = date
    
    @text_content.setter
    def text_content(self, new_text_content_list):
        self._text_content = new_text_content_list
    
    @category.setter
    def category(self, new_category_list):
        self._category = new_category_list
    
