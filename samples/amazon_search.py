import json
from music_browser.plugins import AmazonPlugin
from music_browser.serializer import MusicBrowserSerializer


def amazon_search(query):
    amazon = AmazonPlugin()
    tracks = amazon.search(query)

    for simple_track in tracks:
        print(simple_track)

    return tracks


if __name__ == "__main__":
    tracks = amazon_search("Lovers on the sun")

    with open("samples_output/amazon_tracks.json", "w") as amazon_tracks:
        json.dump(tracks, amazon_tracks, indent=4, cls=MusicBrowserSerializer)
