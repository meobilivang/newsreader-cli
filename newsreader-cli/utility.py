def text_convert(input) -> str:
    """
        input: raw scraped html
    """
    return "" if input is None else input.get_text().strip()

def text_sanitizer(input) -> str:
    return input.replace('\n', '').replace('\r', '').strip()