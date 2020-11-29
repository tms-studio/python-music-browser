import json
from music_browser import MusicBrowser
from music_browser.plugins import SpotifyPlugin
from music_browser.serializer import MusicBrowserSerializer


def browser_search(query):
    spotify = SpotifyPlugin(
        client_id="97e316da02e94644b332c3ad77554c68", client_secret="9b999c62cf324a428a335a7d87b3d0a9"
    )
    browser = MusicBrowser(search_plugin=spotify, completion_plugins=[spotify])
    tracks = browser.search(query)

    for simple_track in tracks:
        print(simple_track)

    return tracks


if __name__ == "__main__":
    tracks = browser_search("Lovers on the sun")

    with open("samples_output/browser_tracks.json", "w") as spotify_tracks:
        json.dump(tracks, spotify_tracks, indent=4, cls=MusicBrowserSerializer)
