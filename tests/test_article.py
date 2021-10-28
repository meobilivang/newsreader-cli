import pytest
from newsreadercli.article import Article

@pytest.mark.parametrize(
        "a, b, expected",
    [
        [2, 1, 1], [-1, 1, -2]
    ]
)
def test_article():
    article = Article()
    pass