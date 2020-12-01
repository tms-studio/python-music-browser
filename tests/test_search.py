from samples.amazon_search import amazon_search
from samples.deezer_search import deezer_search
from samples.spotify_search import spotify_search
from samples.browser_search import browser_search


def test_amazon_search():
    amazon_search("Lovers on the sun")


def test_deezer_search():
    deezer_search("Lovers on the sun")


def test_spotify_search():
    spotify_search("Lovers on the sun")


def test_browser_search():
    browser_search("Lovers on the sun")
