from .base import Plugin


class SpotifyPlugin(Plugin):
    @property
    def known_fields(self):
        return {"title", "artist", "album"}

    def query(self, query_params, query_fields):
        pass
