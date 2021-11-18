import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="933d442fd6d6495c9a48f5a32dcb14fe",
                                                           client_secret="bd6f5b38b8fd41c5a51b527ccebb12f6"))
results = sp.search(q="weezer", limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])
