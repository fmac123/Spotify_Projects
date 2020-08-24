import requests
import json

endpoint_url = "https://api.spotify.com/v1/recommendations?"
access_token = "BQCEAatFPNEnaM9g1Bxf5CVyDlUReEvYGAVAYX0FlVcq6FrXXazU4LQmmwBfA_Z-RnJSsqJbf0l0ml5Yu35IPh93TdPbIY6Np7FS6O0LC6LrgIXzol0zHneVvH-plUIEEnaK8uRbnKdV6m-R-vxU_9IzvlWNPIa9pb27d7yR9Zke6Q"
user_id = "rhythm_20"

#FILTERS
limit = 10 #no. of songs
market = "AU" #country
seed_genres = "indie"
seed_artists = "1btWGBz4Uu1HozTwb2Lm8A"  # ID for Hippo Campus

uris = [] 

#QUERY FOR SONGS
query = f'{endpoint_url}limit={limit}&market={market}&seed_artists={seed_artists}'

response = requests.get(query,
               headers={"Content-Type":"application/json",
                        "Authorization":f"Bearer {access_token}"})

print(response)

json_response = response.json()
for i,j in enumerate(json_response['tracks']):
    uris.append(j['uri'])
    print(f"{i+1}) \"{j['name']}\" by {j['artists'][0]['name']}")




#CREATE A NEW PLAYLIST

endpoint_url = f"https://api.spotify.com/v1/users/{user_id}/playlists"

request_body = json.dumps({
          "name": "Indie bands like Hippo Campus and Glass Animals but using Python",
          "description": "My first programmatic playlist, yooo!",
          "public": False
        })
response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {access_token}"})

url = response.json()['external_urls']['spotify']
print(response.status_code)


# FILL THE NEW PLAYLIST WITH THE RECOMMENDATIONS

playlist_id = response.json()['id']

endpoint_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

request_body = json.dumps({
          "uris" : uris
        })
response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {access_token}"})

print(response.status_code)

print(f'Your playlist is ready at {url}')
