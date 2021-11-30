import requests
import json


# reads client info from separate file
def get_client_info():
    with open("spotify_creds.json", "r") as file:
        data = json.loads(file.read())
        return data["client_id"], data["client_secret"]


# generates the html code for a Spotify play button for a specific track
def generate_play_button(track_id):
    html = f'<iframe src="https://open.spotify.com/embed/track/{track_id}?utm_source=generator" width="100%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>'
    return html


class APICall:

    def __init__(self):
        self.base_url = "https://api.spotify.com/v1"
        self.client_id, self.client_secret = get_client_info()
        self.access_token = "empty"

    # generates and sets access token for the Spotify API
    def get_access_token(self):
        url = "https://accounts.spotify.com/api/token"  # note that this is not from the base url

        request_body = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }

        response = requests.post(url, data=request_body)
        self.access_token = response.json()["access_token"]

    # returns a song object dictionary with keys: id, artists, name, link
    def get_song(self, query):
        url = self.base_url + f"/search?q={query}&type=track"
        headers = {
            "Authorization": "Bearer " + self.access_token
        }

        response = requests.get(url, headers=headers)

        # sets or resets expired access token and retries request
        if response.status_code == 401:
            self.get_access_token()
            headers = {
                "Authorization": "Bearer " + self.access_token
            }
            response = requests.get(url, headers=headers)

        # just grabs the first track available
        first_result = response.json()["tracks"]["items"][0]

        song_id = first_result["id"]
        song_artists = [item["name"] for item in first_result["artists"]]
        song_name = first_result["name"]
        song_link = generate_play_button(song_id)

        song_object = {
            "id": song_id,
            "artists": song_artists,
            "name": song_name,
            "link": song_link
        }
        return song_object


# EXAMPLE program
# -------------------------------------------
if __name__ == "__main__":

    # init
    client = APICall()

    # generated song object
    song1 = client.get_song("Take My Breath Weeknd")

    # showcasing dictionary
    for item in song1.keys():
        print(f"{item}: {song1[item]}")

    print()

    # a second track
    song2 = client.get_song("Hurt Johnny Cash")

    for item in song2.keys():
        print(f"{item}: {song2[item]}")
