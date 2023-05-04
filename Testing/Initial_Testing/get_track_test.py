import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

with open("credentials.json") as infile:
        auth = json.load(infile)
        client_id = auth["client_id"]
        client_secret = auth["client_secret"]

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
track1 = "2CNx8At5NGaUuoZlpmtcp7" # comp track
track2 = "0VjIjW4GlUZAMYd2vXMi3b" # real track
response1 = spotify.track(track1)
response2 = spotify.track(track2)
print(response1["album"]["artists"][0]["name"])
