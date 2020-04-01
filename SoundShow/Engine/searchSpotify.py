CLIENT_ID =  "4bffd52f83ce4f158e0e7c3b3c245f67"
CLIENT_SECRET = "4934a01747584350ae36fd09b8eececb"


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import re
import json
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET))

results = sp.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

def artistForGenres(genres):
    st = sp.recommendations(seed_artists=None, seed_genres=genres, seed_tracks=None, limit=20, country=None)
    with open("spot.json",  "w+") as spot:
        json.dump(st, spot)
    # regexp = re.compile("spotify:[A-Za-z0-9]+")
    # with open("spot.txt", "w+") as spot:
    #     spot.write(st)
    # tmp = re.search(regexp, st)
    return st
