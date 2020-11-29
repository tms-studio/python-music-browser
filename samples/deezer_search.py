import json
from music_browser.plugins import DeezerPlugin
from music_browser.serializer import MusicBrowserSerializer


def deezer_search(query):
    deezer = DeezerPlugin()
    tracks = deezer.search(query)

    for simple_track in tracks:
        print(simple_track)

    return tracks


if __name__ == "__main__":
    tracks = deezer_search("Lovers on the sun")

    with open("samples_output/deezer_tracks.json", "w") as deezer_tracks:
        json.dump(tracks, deezer_tracks, indent=4, cls=MusicBrowserSerializer)
