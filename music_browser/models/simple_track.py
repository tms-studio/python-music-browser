from dataclasses import dataclass


@dataclass
class Source:
    id: str
    platform: str

    def __json__(self):
        return {"id": self.id, "platform": self.platform}


@dataclass
class SimpleTrack:
    title: str
    artist: str
    album: str
    cover: str
    source: Source

    def __str__(self):
        max_width = 20
        return "SimpleTrack:   %s   %s   %s" % (
            (self.title if len(self.title) < max_width else self.title[: max_width - 3] + "...").ljust(max_width),
            (self.artist if len(self.artist) < max_width else self.artist[: max_width - 3] + "...").ljust(max_width),
            (self.album if len(self.album) < max_width else self.album[: max_width - 3] + "...").ljust(max_width),
        )

    def __json__(self):
        return {
            "title": self.title,
            "artist": self.artist,
            "album": self.album,
            "cover": self.cover,
            "source": self.source,
        }
