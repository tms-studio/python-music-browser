import requests
from typing import List
from urllib.parse import urlencode
from .base import Plugin
from ..models import SimpleTrack


class DeezerPlugin(Plugin):
    """
    Define methods to search tracks on deezer
    and complete metadata from deezer's database.
    """

    @property
    def known_fields(self):
        """
        Return a set of known fields that can be returned by complete() method.
        """
        return set()

    def query(self, track: SimpleTrack) -> object:
        """
        Complete metadata of a track based on simple track data like title, artist, or id.
        """
        pass

    def search(self, query: str) -> List[SimpleTrack]:
        """
        Return list of tracks matching the query.

        Parameters:
            query: String describing what track you are looking for.

        Returns:
            List of tracks known by Deezer that matches the query.
        """
        response = requests.get("https://api.deezer.com/search?" + urlencode({"q": query}))

        tracks = []
        for track_data in response.json()["data"]:
            tracks.append(
                SimpleTrack(
                    album=track_data["album"]["title"],
                    artist=track_data["artist"]["name"],
                    title=track_data["title"],
                    cover="https://e-cdns-images.dzcdn.net/images/cover/%s/264x264-000000-80-0-0.jpg"
                    % track_data["md5_image"],
                    source={"id": str(track_data["id"]), "platform": "deezer"},
                )
            )

        return tracks
