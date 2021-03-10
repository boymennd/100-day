from bs4 import BeautifulSoup
import requests
import spotipy, os
from spotipy.oauth2 import SpotifyOAuth

id = os.environ.get("ID_SPOTIFY")
secret = os.environ.get("KEY_SPOTIFY")


date_choose = input(
    "Which year do you want to travel to(type data in this format YYYY-MM-DD)?"
)
url = f"https://www.billboard.com/charts/hot-100/{date_choose}"
year = date_choose.split("-")[0]
response = requests.get(url=url)
data = BeautifulSoup(response.text, "html.parser")
name_song = data.find_all(
    name="span", class_="chart-element__information__song text--truncate color--primary"
)
sp = spotipy.Spotify(
    oauth_manager=SpotifyOAuth(
        client_id=id,
        client_secret=secret,
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        show_dialog=True,
        cache_path="token.txt",
    )
)
user_id = sp.current_user()["id"]
song_uri_list = []
for song in name_song:
    search = sp.search(q=f"track:{song.string} year:{year}", type="track")["tracks"][
        "items"
    ]
    try:
        song_uri = search[0]["uri"]
        song_uri_list.append(song_uri)
    except IndexError:
        print(f"The song {song.string} not available on spotify!")
playlist = sp.user_playlist_create(
    user=user_id, name=f"Billboard 100 in {date_choose}", public=False
)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uri_list)
print("This is link you want!")
print(playlist["external_urls"]["spotify"])
