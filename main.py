from music_browser import MusicBrowser
from music_browser.plugins import SpotifyPlugin, ISRCPlugin

browser = MusicBrowser(plugins=[SpotifyPlugin(), ISRCPlugin()])
print(browser.known_fields)
