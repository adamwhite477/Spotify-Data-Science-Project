import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

with open("credentials.json") as infile:
        auth = json.load(infile)
        client_id = auth["client_id"]
        client_secret = auth["client_secret"]

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

frank_ocean_uri = "spotify:artist:2h93pZq0e7k5yf4dywlkpM"
drake_uri = "spotify:artist:3TVXtAsR1Inumwj472S9r4"

uris = [frank_ocean_uri, drake_uri]

for uri in uris:
    artist = spotify.artist(uri)
    print("Current Artist...")
    name = artist["name"]
    print(name)
    print("{} popularity: {} (max 100)".format(name, artist["popularity"]))
    print("Amount of followers: {}".format(artist["followers"]["total"]))
    top_tracks = spotify.artist_top_tracks(uri)
    top_track = top_tracks["tracks"][0]["name"]
    print("Top Track: {}".format(top_track))
    print()
    
    
    