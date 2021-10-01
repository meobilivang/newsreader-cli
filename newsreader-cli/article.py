from typing import Text


class Article:
    def __init__(self, title = "Empty Title", url = "Empty URL", description = "Empty Description", text_content = [], date = "Unidentified", category = []):
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
    
    def __get_content__(self):
        return self.text_content

    def __get_date__(self):
        return self.date
    
    def __get_catergory(self):
        return self.category
    
    def __set_date(self, date):
        self.date = date

    def __insert_text_content_(self, new_text_content):
        self.text_content.append(new_text_content)
    
    
    def __insert_category(self, new_category):
        self.category.insert(new_category)
        
    
