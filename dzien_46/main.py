
from bs4 import BeautifulSoup
import requests
import spotipy
import os

SPOTIFY_CLIENT_ID = os.environ['SPOTIFY_CLIENT_ID']
SPOTIFY_CLIENT_SECRET = os.environ['SPOTIFY_CLIENT_SECRET']
SPOTIFY_CLIENT_USERNAME = os.environ['SPOTIFY_CLIENT_USERNAME']


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(url=f'https://www.billboard.com/charts/hot-100/{date}', headers=header)

soup = BeautifulSoup(response.text, 'html.parser')

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

print(song_names)

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://open.spotify.com/",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=SPOTIFY_CLIENT_USERNAME,
    )
)

user_id = sp.current_user()["id"]



song_uris = []

for song in song_names:
    song_uri = sp.search(q=f"track: {song} year {date.split('-')[0]}", limit=1, type='track')
    # pprint(song_uri)
    try:
        uri = song_uri["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

print(song_uris)

playlist = sp.user_playlist_create(user = user_id, name = f"{date} Billboard 100", public=False)


sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris, position=None)