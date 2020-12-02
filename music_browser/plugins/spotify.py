import time
import requests
from base64 import b64encode
from typing import List
from urllib.parse import urlencode
from .base import Plugin
from ..models import SimpleTrack
from ..exceptions import MusicBrowserException


class SpotifyAuthentication:
    """
    Manage token based authentication for Spotify Plugin.
    """

    def __init__(self, client_id: str, client_secret: str):
        """
        Store client_id and client_secret encoded in base64.

        Arguments:
            client_id: Identifier of your application obtained by declaring your app to Spotify.
            client_secret: Secret key of your application obtained by declaring your app to Spotify.
        """
        # workout base64 header required by spotify to authenticate using client credentials.
        self.basic_token = b64encode(("%s:%s" % (client_id, client_secret)).encode("utf-8")).decode("utf-8")
        # token lazy loading. Indicates that a new token must be issued from now.
        self.expires = time.time()

    def authenticate(self):
        """
        Issue a fresh access token and update expiration counter.
        """
        # exchange client credentials for a token against spotify accounts API.
        response = requests.post(
            "https://accounts.spotify.com/api/token",
            data={"grant_type": "client_credentials"},
            headers={
                "Authorization": "Basic %s" % self.basic_token,
                "Content-Type": "application/x-www-form-urlencoded",
            },
        )
        # ensure that proper token response has been received
        if response.status_code != 200:
            raise MusicBrowserException("Unable to retrieve access_token from Spotify API.")

        token_data = response.json()
        # store useful token data as properties
        self.access_token = token_data["access_token"]
        self.expires = time.time() + token_data["expires_in"]

    def has_expired(self) -> bool:
        """
        Check if stored token is still valid.

        Returns:
            `true` if currently stored token is valid, `false` otherwise.
        """
        # check if expiration time is passed
        return self.expires < time.time()

    def get_token(self) -> str:
        """
        Returns:
            A valid access token. If token was stale, it is refreshed before being returned.
        """
        # ensure that known token is up-to-date
        if self.has_expired():
            self.authenticate()
        # ... then return valid access token
        return self.access_token


class SpotifyPlugin(Plugin):
    """
    Define methods to search tracks on spotify
    and complete metadata from spotify's database.
    """

    def __init__(self, client_id: str, client_secret: str):
        """
        Arguments:
            client_id: Identifier of your application obtained by declaring your app to Spotify.
            client_secret: Secret key of your application obtained by declaring your app to Spotify.
        """
        self.auth = SpotifyAuthentication(client_id, client_secret)

    @property
    def known_fields(self):
        """
        Return a set of known fields that can be returned by complete() method.
        """
        return {"title", "artist", "album"}

    def query(self, query_params, query_fields):
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
            List of tracks known by Spotify that matches the query.
        """

        r = requests.get(
            "https://api.spotify.com/v1/search?" + urlencode({"type": "track", "query": query}),
            headers={"Authorization": "Bearer %s" % self.auth.get_token()},
        )

        tracks = []

        for track_data in r.json()["tracks"]["items"]:
            tracks.append(
                SimpleTrack(
                    album=track_data["album"]["name"],
                    artist=track_data["artists"][0]["name"],
                    title=track_data["name"],
                    cover=track_data["album"]["images"][0]["url"],
                    source={"id": track_data["id"], "platform": "spotify"},
                )
            )

        return tracks
