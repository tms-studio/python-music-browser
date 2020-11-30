# python-music-browser

> Python library to query music metadata from various sources.

## Plugins features

### Browse tracks

You can use plugin to issue any tracks provider (like Spotify) a query.

```python
from music_browser.plugins import SpotifyPlugin

spotify = SpotifyPlugin(
    client_id="97e316da02e94644b332c3ad77554c68", client_secret="9b999c62cf324a428a335a7d87b3d0a9"
)
tracks = spotify.search(query)

for simple_track in tracks:
    print(simple_track)
```

As a result you will get a list of [SimpleTrack](#simpletrack), an object containing most basic properties of a track.

### Complete track metadata

Coming soon...

## Make your own plugin

Coming soon...

## Objects structure

### SimpleTrack

A [SimpleTrack](#simpletrack) object has the following structure. It is returned when a list of tracks is asked to give a quick preview of each track. If later you would like to query more details, refere to [FullTrack](#fulltrack).

```python
simple_track.__json__()
{
    "title": "Lovers On the Sun (Metal Version)",
    "artist": "UMC",
    "album": "Lovers On the Sun (Metal Version)",
    "cover": "https://i.scdn.co/image/ab67616d0000b273fa786b81f34442a68738be05",
    "source": {
        "id": "5fVCKGCQcZ1VPJNZrWqCO0",
        "platform": "spotify"
    }
},
```

### FullTrack

Coming soon...

## TODO

* Run pre-publish checks using python matrix instead of a specific version
* Create separate workflow for [push, pull_request] and [tags]
