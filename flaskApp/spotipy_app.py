import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

def add_songs_to_playlist(country, artists):
    cid= '16b80191a35b48778bb2df4b6f9cee65'
    secret = '19fa57fbd8c3431983c1af5ccc8359e4'
    redirect = "http://localhost/"
    playlist_id = '4IHRZLGxuLYWk5IrHqorJg'
    scope = 'playlist-modify-public, playlist-modify-private'
    username = 'brielle.dolphin'
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager, auth_manager=SpotifyOAuth(client_id = cid, client_secret = secret, scope=scope, redirect_uri = redirect))

    #create playlist
    sp.user_playlist_create(user = username, name = country)
    results = sp.current_user_playlists(limit=50)
    for i, item in enumerate(results['items']):
        print("%d %s" % (i, item['name']))
        if (item['name'] == country):
            playlist_id = item ['id']
            break

    track_id = []
    track_names = []
    for artist in artists:
        for i in range(0,5):
            query = f"artist:{artist}"
            track_results = sp.search(q=query, type='track', limit=10,offset=i)
            #print ("len" + str(len(track_results["tracks"]["items"])))
            if (len(track_results["tracks"]["items"]) > i):
                track_uri = track_results["tracks"]["items"][0]['uri']
                track_name = track_results["tracks"]["items"][0]['name']
                track_names.append(track_name)
                track_id.append(track_uri)
    sp.playlist_add_items( playlist_id = playlist_id, items = track_id)   
    for track in track_names:
        print (track)
    return ("https://open.spotify.com/playlist/" + str (playlist_id))

#print (add_songs_to_playlist("US", ["Taylor Swift", "AJR"]))