import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials



def findSongs ():
    cid= '16b80191a35b48778bb2df4b6f9cee65'
    secret = '19fa57fbd8c3431983c1af5ccc8359e4'
    redirect = "http://localhost/"
    playlist_id = '4IHRZLGxuLYWk5IrHqorJg'
    scope = 'playlist-modify-public, playlist-modify-private'
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager, auth_manager=SpotifyOAuth(client_id = cid, client_secret = secret, scope=scope, redirect_uri = redirect))

    #create playlist

    track_id = []
    track_names = []
    for i in range(0,5):
        track_results = sp.search(q='artist:AJR', type='track', limit=1,offset=i)
        track_uri = track_results["tracks"]["items"][0]['uri']
        track_name = track_results["tracks"]["items"][0]['name']
        track_names.append(track_name)
        track_id.append(track_uri)
    sp.playlist_add_items( playlist_id = playlist_id, items = track_id)   
    for track in track_names:
        print (track)

findSongs()