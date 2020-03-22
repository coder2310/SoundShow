import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import re
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
        print(album['name'])




# Gets 30 second samples and cover art for the top 5 tracks for the given artists
def samples (artist_uri):
    results = sp.artist_top_tracks(artist_uri)

    for track in results['tracks'][:5]:
        print('track    : ' + track['name'])
        print('audio    : ' + track['preview_url'])
        print('cover art: ' + track['album']['images'][0]['url'])



#prints out the cover image of the artist and returns the artist_id
def artistImage(artist_name):
    if len(sys.argv) > 1:
        name = ' '.join(sys.argv[1:])
    else:
        name = 'Radiohead'

    results = sp.search(q='artist:' + artist_name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0]
        artistId = artist['id']
        print(artist['name'], artist['images'][0]['url'])
    return  artistId


#gives us the artist_uri
def artist_URIs(artist_id):
    artist_uri = "spotify:artist:"
    artist_uri = artist_uri + artist_id
    return artist_uri


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


def main():
    artist = 'Bad Bunny'
    artists_uri = artist_URIs(artistImage(artist))
    samples(artists_uri)
    print(getrelatedArtists(artistImage(artist)))
    artist = 'Kendrick Lamar'
    track = 'Loyalty'
    track_uri = getURI(artist, track)
    print(track_uri)



if __name__ == "__main__":
    main()
