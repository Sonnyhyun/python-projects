import requests
import spotipy
import pprint
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECT_URL = "http://example.com"

response = requests.get("https://www.billboard.com/charts/hot-100/2000-08-12")
web_page = response.text


soup = BeautifulSoup(web_page, "html.parser")

title = soup.select("li ul li h3")
song_titles = [song.getText().strip() for song in title]




sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id = CLIENT_ID,
        client_secret = CLIENT_SECRET,
        redirect_uri = REDIRECT_URL,
        scope = "playlist-modify-private",
        cache_path = "DAY46/token.txt",
        show_dialog = True
    )
)

user_id = sp.current_user()['id']
music_travel = input("음악여행 몇 년도로 갈래 YYYY-MM-DD?")
song_names = ["The list of song", "titles from your", "web scrape"]

song_url = []
year = music_travel.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        url = result["tracks"]
        song_url.append(url)
        
    except IndexError:
        print(f"A song {song} that you want to hear is not founded, so skip")


playlists = sp.user_playlist_create(user=user_id, name=f"{music_travel} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlists['id'], items=song_url)
