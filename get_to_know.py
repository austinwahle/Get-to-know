import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyAuthBase
import spotipy.util as util
from variables import user, client_id, client_secret

username = user
cid = client_id
secret = client_secret

scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username, scope,client_id=cid,client_secret=secret,redirect_uri='http://127.0.0.1:9090')
sp = spotipy.Spotify(auth=token)

artist_name = input('Enter an artist you\'d like to get to know')
artist = sp.search(artist_name, type = 'artist', market = 'US')
artist_id = artist['artists']['items'][0]['id']

playlist_name = f'Get to Know {artist_name}'
sp.user_playlist_create(username, playlist_name)

playlist_id = None
playlists = sp.user_playlists(username)['items']
for playlist in playlists:
    if playlist['name']==playlist_name:
        playlist_id = playlist['id']

track_list = []
track_names = []
tracks = sp.artist_top_tracks(artist_id)['tracks']
for track in tracks:
    track_list.append(track['id'])
    track_names.append(track['name'])



sp.user_playlist_add_tracks(username, playlist_id, track_list)
print(f'A playlist called \"{playlist_name}\" has been added to your library with {track_names[0]} and 9 more songs by {artist_name}')
