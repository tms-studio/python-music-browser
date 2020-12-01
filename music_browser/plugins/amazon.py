import requests
from typing import List
from .base import Plugin
from ..models import SimpleTrack
from ..exceptions import MusicBrowserException

headers = {
    "x-amzn-device-family": "WebPlayer",
    "x-amzn-device-time-zone": "+01:00",
    "x-amzn-timestamp": "1606815294665",
    "x-amzn-application-version": "1.0.4821.0",
    "x-amzn-device-width": "1920",
    "x-amzn-device-id": "26248146527924562",
    "x-amzn-weblab-id-overrides": "",
    "x-amzn-authentication": '{"interface":"ClientAuthenticationInterface.v1_0.ClientTokenElement","accessToken":""}',
    "x-amzn-csrf": (
        '{"interface":"CSRFInterface.v1_0.CSRFHeaderElement","token":"yaeE4zpRbYx81h+tGbctPmSFjFl+MnkCH04w1lsmaIA="'
        ',"timestamp":"1606815099181","rndNonce":"237549537"}'
    ),
    "x-amzn-request-id": "42fa8418-030a-48fa-a415-2558fd04c0e3",
    "x-amzn-os-version": "1.0",
    "x-amzn-session-id": "259-3324251-4658301",
    "x-amzn-user-agent": (
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36"
    ),
    "x-amzn-music-domain": "music.amazon.fr",
    "user-agent": (
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/87.0.4280.66 Mobile Safari/537.36"
    ),
    "x-amzn-device-height": "1080",
    "x-amzn-device-language": "fr_FR",
    "x-amzn-affiliate-tags": "undefined",
    "x-amzn-referer": "music.amazon.fr",
    "x-amzn-device-model": "WEBPLAYER",
}


class AmazonPlugin(Plugin):
    @property
    def known_fields(self):
        return set()

    def query(self):
        pass

    def search(self, query: str) -> List[SimpleTrack]:
        params = (
            ("keyword", query),
            ("userHash", '{"level":"LIBRARY_MEMBER"}'),
        )

        response = requests.get(
            "https://eu.web.skill.music.a2z.com/api/searchCatalogTracks", headers=headers, params=params
        )
        # ensure that proper token response has been received
        if response.status_code != 200:
            raise MusicBrowserException("Unable to retrieve access_token from Spotify API.")

        tracks_data = response.json()["methods"][0]["template"]["widgets"][0]["items"]

        tracks = []
        for track_data in tracks_data:
            tracks.append(
                SimpleTrack(
                    title=track_data["primaryText"]["text"],
                    artist=track_data["secondaryText"],
                    cover=track_data["image"],
                    source={"id": track_data["iconButton"]["observer"]["storageKey"], "platform": "amazon"},
                )
            )
        return tracks
