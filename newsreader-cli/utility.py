def text_convert(input) -> str:
    """
        input: raw scraped html
    """
    return "" if input is None else input.get_text().strip()
