import requests
import json

# TEMPORARY CREDENTIAL HARD-CODING
client_id = "87b9cbe45bf0454eb66c99e5a3ae1ddd"
client_secret = "336ef5841cb64042ad2e5ebb2c867f8a"

# reads client info from separate file
def get_client_info():
        return client_id, client_secret


# generates the html code for a Spotify play button for a specific track
def generate_play_button(track_id):
    html = f'https://open.spotify.com/embed/track/{track_id}?utm_source=generator'
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
