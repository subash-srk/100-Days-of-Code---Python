from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


URL = "https://www.billboard.com/charts/hot-100/"
CLIENT_ID = ""
CLIENT_SECRET = ""
USER_NAME = ""

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id= CLIENT_ID,
        client_secret= CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=USER_NAME,
    )
)
user_id = sp.current_user()["id"]

date = input("Enter the date [yyyy-mm-dd]: ")

response = requests.get(url=f"{URL}/{date}/")
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

top_100_tags = soup.select("li ul li h3")
# print(top_100_tags)
top_100_songs = [songs.getText().strip() for songs in top_100_tags]
print(top_100_songs)

song_uris = []
year = date.split("-")[0]

for song in top_100_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)