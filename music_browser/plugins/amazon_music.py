from .base import Plugin

class AmazonMusicPlugin(Plugin):
    def search(self, query:str):
        params = (
            ('keyword', query),
            ('userHash', '{"level":"LIBRARY_MEMBER"}'),
        )

        response = requests.get('https://eu.web.skill.music.a2z.com/api/searchCatalogTracks', headers=headers, params=params)
        assert response.status_code == 200

        tracks_data = response.json()["methods"][0]["template"]["widgets"][0]["items"]

        tracks = []
        for track_data in tracks_data:
            tracks.append({
                "title": track_data["primaryText"]["text"],
                "artist": track_data["secondaryText"],
                "cover": track_data["image"],
                "source": {
                    "id": track_data["iconButton"]["observer"]["storageKey"],
                    "platform": "amazon"
                }
            })
        return tracks
