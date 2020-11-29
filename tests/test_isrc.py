import pytest
from music_browser import MusicBrowser
from music_browser.exceptions import UnknownField

REQUIRED = True
OPTIONAL = False


def test_browser_interface():
    """
    Check that browser raises unknownfield when no plugin declare to return this field.
    """
    browser = MusicBrowser()
    with pytest.raises(UnknownField):
        browser.query(title="Where is the love?").fields(isrc=REQUIRED).result()
