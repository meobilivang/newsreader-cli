def text_convert(input) -> str:
    """
        input: raw scraped html
    """
    return "" if input is None else input.get_text().strip()

def text_sanitizer(input) -> str:
    """
        input: a string input
        
        Remove all the newlines, whitespaces from string
    """
    return input.replace('\n', '').replace('\r', '').strip()