import requests

base_url = "https://api.spotify.com/v1"

# TEMPORARY CREDENTIAL HARD-CODING
client_id = "87b9cbe45bf0454eb66c99e5a3ae1ddd"
client_secret = "336ef5841cb64042ad2e5ebb2c867f8a"


# generates an access token for the Spotify API
def get_access_token():
    url = "https://accounts.spotify.com/api/token"  # note that this is not from the base url

    request_body = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }

    response = requests.post(url, data=request_body)

    return response.json()


# gets the id of a TRACK based on a search query
def get_id(token, query):
    url = base_url + f"/search?q={query}&type=track"
    headers = {
        "Authorization": "Bearer " + token
    }

    response = requests.get(url, headers=headers)

    first_result = response.json()["tracks"]["items"][0]

    for item in first_result.keys():
        print(item)

    print(first_result["id"])
    print(first_result["artists"])
    print(first_result["name"])

    return first_result["id"]


# gets a track by track id
def get_track(token, track_id):
    url = base_url + f"/tracks/{track_id}"
    headers = {
        "Authorization": "Bearer " + token
    }

    response = requests.get(url, headers=headers)

    # print(response)
    # print(response.text)
    # print()

    return response.json()["external_urls"]["spotify"]


# generates the html code for a Spotify play button for a specific track
def generate_play_button(track_id):
    html = f"https://open.spotify.com/embed/track/{track_id}?utm_source=generator"
    return html


# returns a song object dictionary with keys: id, artists, name, link
def get_song(token, query):
    url = base_url + f"/search?q={query}&type=track"
    headers = {
        "Authorization": "Bearer " + token
    }

    response = requests.get(url, headers=headers)

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
