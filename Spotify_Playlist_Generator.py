import requests
import json

endpoint_url = "https://api.spotify.com/v1/recommendations?"
access_token = "BQDO6aYMkQzi_iw3Jmc8ca3N9CTzSze1lBL3E6QLHWKa_EWUCOapJQG1t60FwzAxC9n8tuhKR_fvixvvqh4M0_RBDa0NTSJbdW1v3ilF2abOiG-EG1j6hQbnqWfR4FtBZb3mevXI4JWIKRPDf7wl2DLAZqwBYIgF8OyjnfnN9v2-iA"
user_id = "rhythm_20"

#FILTERS
limit = 10 #no. of songs
market = "AU" #country
seed_genres = "indie"
seed_artists = "1btWGBz4Uu1HozTwb2Lm8A,4yvcSjfu4PC0CYQyLy4wSq,0Ou0138wEd8XWebhc4j7O0"   # ID for Hippo Campus, Glass Animals, San Cisco
popularity=40
valence=0.8 
uris = [] 

#QUERY FOR SONGS
query = f'{endpoint_url}limit={limit}&market={market}&popularity={popularity}&valence={valence}&seed_artists={seed_artists}'

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
          "name": "Happy??",
          "description": "Magic",
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
