from .base import Plugin


class ISRCPlugin(Plugin):
    @property
    def known_fields(self):
        return {"isrc"}

    def query(self, query_params, query_fields):
        pass
