import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import re
import json
CLIENT_ID = '472db3710d084b36926341acefd1311e'
CLIENT_SECRET = '8dd4c8534b69424681c137b8af0dd2cb'
USER = '31h25u3gvkjfkgctbsb4hv5mdb4i?si=QmrACCNSS7qa927dwUICTA'

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

country = 'US'
language = ''
locale = ''
limit = 10
offset = 0

fav_artists = []
artists_uri = {}   #key = artist name  && value = artist_uri



# Gives us the track URI
def getURI(artist, track):

    track_id = sp.search(q='artist:' + artist + ' track:' + track, type='track')
    res = dict((k, track_id[k]) for k in ['tracks'] if k in track_id)
    st = str(res)
    regexp = re.compile("spotify:artist:[A-Za-z0-9]+")
    tmp = re.search(regexp, st)
    return tmp.group()


#List all the name of the Album released by the artist
def printAlbumNames(artist_uri):

    results = sp.artist_albums(artist_uri, album_type='album')
    albums = results['items']
    
    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])

    for album in albums:
        print(album)

def get_album_names(artist_uri):
    results = sp.artist_albums(artist_uri, limit = 3, album_type='album')
    albums = results['items']
    while  results['next']:
        results = sp.next(results)
        #print(type(results), count)
        albums.extend(results['items'])
        
    album_results = []
    album_names = set()
    counter = 0
    for album in albums:
        counter += 1
        if counter == 3:
            break
        form = {
            "name" : None,
            "release date": None,
            "url" : None,
        }
        if album["name"] not in album_names:
            try:
                if album["name"] != None and album["release_date"] != None \
                and album["external_urls"]["spotify"] != None:
                    form["name"] = album["name"]
                    form["release date"]  = album["release_date"]
                    form["url"] = album["external_urls"]["spotify"]
                    album_results.append(form)
                    album_names.add(form["name"])
            except:
                pass
        
    return album_results


        

# Gets 30 second samples and cover art for the top 5 tracks for the given artists
def samples(artist_uri):
    results = sp.artist_top_tracks(artist_uri)
    top_tracks = []
    for track in results['tracks'][:5]:
        form = {
            "track": None,
            "audio": None
        }
        form["track"] = track["name"]
        form["audio"] = track["preview_url"]
        if form["track"] != None and form["audio"] != None:
            top_tracks.append(form)
    return top_tracks



#prints out the cover image of the artist and returns the artist_id
def artistImage(artist_name):
    # if len(sys.argv) > 1:
    #     name = ' '.join(sys.argv[1:])
    # else:
    #     name = 'Radiohead'
    results = sp.search(q='artist:' + artist_name, type='artist')
    items = results['artists']['items']
    img_url = None
    if len(items) > 0:
        try:
            artist = items[0]
            img_url = artist['images'][0]['url']
        except:
            pass
        #print(artist['name'], artist['genres'], artist['images'][0]['url'])
    return img_url



def artistForGenres(genres):
    for ndx in range(len(genres)):
        genres[ndx] = genres[ndx].lower()
        genres[ndx] = genres[ndx].replace(" ", "-")
    st = sp.recommendations(seed_artists=None, seed_genres=genres, seed_tracks=None, limit=20, country=None)
    artists = []
    count = 0
    for elem in st["tracks"]:
        artists_format = {
        "artist" : None,
        "link" : None,
        "albums": None,
        "img_link": None,
        "uri" : None,
        "top_tracks": None
        }
        artists_format["artist"] = elem["album"]["artists"][0]["name"]
        artists_format["link"] = elem["album"]["artists"][0]["external_urls"]["spotify"]
        artists_format["uri"] =  elem["album"]["artists"][0]["uri"]
        artists_format["img_link"] = artistImage(artists_format["artist"])
        artists_format["albums"] = get_album_names(artists_format["uri"])
        artists_format["top_tracks"] = samples(artists_format["uri"])
        # has_none = False
        # for keys in artists_format.keys():
        #     if artists_format[keys] == None:
        #         has_none = True
        #     if artists_format[keys] == []:
        #         has_none = True

        # if not has_none:
        artists.append(artists_format)
        count += 1
        if count > 10:
            break
    return artists


#gives us the artist_uri
def artist_URIs(artist_id):
    artist_uri = "spotify:artist:"
    artist_uri = artist_uri + artist_id
    return artist_uri

# this fucntion is going to be used if they 
# didnt select music as their interest
# it will look for things such as podcasts
def search_other(search_term):
    results = sp.search(q = search_term, type = "show")
    print(results)
#List all the names tracks with the name of the album
#sp = spotipy.Spotify()
def printTrackNames(album):

    sp.trace = False
    # find album by name
    results = sp.search(q="album:" + album, type="album")

    # get the first album uri
    album_id = results['albums']['items'][0]['uri']

    # get album tracks
    tracks = sp.album_tracks(album_id)
    for track in tracks['items']:
        print(track['name'])



# Gets the AlbumID
def getAlbumId(album_id):
    sp.trace = False
    return sp.album(album_id)


#Gets related Artists
def getrelatedArtists(artist_id):
    sp.trace = False
    return sp.artist_related_artists(artist_id)


#Gets related Artists' Top tracks
def getRelatedArtists(artist_id, country):
    sp.trace = False
    return sp.artist_top_tracks(artist_id, country)


#Gets a list of new album releases featured in Spotify
def spotifyFeaturedAlbums(country, locale, limit, offset):
    sp.trace = False
    return sp.categories(country, locale, limit, offset)



