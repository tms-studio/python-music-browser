from .query import TrackQuery


class MusicBrowser:
    """
    Object that abstract plugins usage to query tracks metadata from multiple sources.

    Keywords Arguments:
        plugins -- (list) Plugins ordered by priority used to fetch metadata.
    """

    def __init__(self, plugins=None):
        self.plugins = []
        self.known_fields = set()

        if plugins:
            # register plugins that improve MusicBrowser sources
            for plugin_module in plugins:
                self.use_plugin(plugin_module)

    def query(self, query_string=None, title=None, artist=None, spotify_id=None):
        """
        Keywords Arguments:
            query_string -- (str) What you would type in a browser to search this track.
            title -- (str) Title of the track.
            artist -- (str) Name of the artist who created this track.

        Returns:
            track_query -- An object used to do lazy loading of tracks metadata.
        """
        return TrackQuery(self.plugins).query(
            query_string=query_string, title=title, artist=artist, spotify_id=spotify_id
        )

    def use_plugin(self, plugin):
        """
        Declare the use of the plugin.
        """
        self.plugins.append(plugin)

        for field in plugin.known_fields:
            self.known_fields.add(field)
