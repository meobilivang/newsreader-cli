import pytest

from newsreadercli import Article
from .test_data.articles_test_data import data

def test_article():
    
    article_1 = Article(
        data.article_1['title'],
        data.article_1['url'],
        data.article_1['description'],
        data.article_1['text_content'],
        data.article_1['date'],
        data.article_1['category']
    )

    assert article_1.title == data.article_1['title']
    assert article_1.url == data.article_1['url']
    assert article_1.description == data.article_1['description']
    assert article_1.text_content == data.article_1['text_content']
    assert article_1.date == data.article_1['date']
    assert article_1.category == data.article_1['category']