import pytest
from music_browser import MusicBrowser
from music_browser.exceptions import MusicBrowserException


def test_get_isrc_by_query():
    """
    Check that correct query returns the right ISC
    """
    browser = MusicBrowser()
    assert (
        browser.query_isrc(query="David Guetta - Lovers on the sun") == "GB28K1400089"
    )


def test_get_isrc_by_author_and_title():
    """
    Check that correct query returns the right ISC
    """
    browser = MusicBrowser()
    assert (
        browser.query_isrc(author="David Guetta", title="Lovers on the sun")
        == "GB28K1400089"
    )


def test_get_isrc_by_author_title_and_query():
    """
    Check that illegal query return an error.
    Only one of (author/title)/query should be passed.
    """
    browser = MusicBrowser()

    with pytest.raises(MusicBrowserException):
        browser.query_isrc(
            author="David Guetta",
            title="Lovers on the sun",
            query="David Guetta - Lovers on the sun",
        )
