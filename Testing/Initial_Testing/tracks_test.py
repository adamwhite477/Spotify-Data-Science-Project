import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

with open("credentials.json") as infile:
        auth = json.load(infile)
        client_id = auth["client_id"]
        client_secret = auth["client_secret"]

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

frank_ocean_uri = "spotify:artist:2h93pZq0e7k5yf4dywlkpM"
results = spotify.artist_top_tracks(frank_ocean_uri)




print("Top 5 Frank Ocean tracks")
for track in results["tracks"][:5]:
    print("track: ", track["name"])
    print("popularity num: ", track["popularity"])
    
    
print("Amt of followers")
artist = spotify.artist(frank_ocean_uri)
total_followers = artist["followers"]["total"]
print(total_followers)


print("Artist popularity")
popularity = artist["popularity"]
print(popularity)

'''
drake_uri = "spotify:artist:3TVXtAsR1Inumwj472S9r4"
drake_results = spotify.artist_top_tracks(drake_uri)


print("\nDrake Tracks")
for track in drake_results["tracks"][:5]:
    print("track: ", track["name"])
    print("popularity num: ", track["popularity"])
    '''