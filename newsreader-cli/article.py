class Article:
    def __init__(self, title = "Empty Title", url = "Empty URL", description = "Empty Description", content = "Empty Content"):
        self.title = title
        self.url = url
        self.description = description
        self.content = content

    def __get_title__(self):
        return self.title
    
    def __get_url__(self):
        return self.url
    
    def __get_description__(self):
        return self.description
    
    def __get_content__(self):
        return self.content
    
