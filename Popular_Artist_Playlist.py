import requests
import json

endpoint_url = "https://api.spotify.com/v1/recommendations?"
# https://developer.spotify.com/console/get-recommendations/ SCOPE: 'playlist-modify-private' and 'user-top-read'
access_token = "BQDjyF_pVR9A6ViWOpxKi9Zaeyhss7akTfWnY9nvdsl5hPlBYVFU3y3Cz8pZo40pPuvY9GRU9cGDZ7b25RsE10FlnUW-VNt9YSkQ4QRqpHYs-ZtQoklCVtv_4z1P7jSEvGRxsoljBlqurTZqA7sf25gj-Iu_4kRjbXNFFubYF2qlAfyanlc"
user_id = "rhythm_20"

limitsong = 2
limitartist = 3
personal_artist_url = f'https://api.spotify.com/v1/me/top/artists?limit={limitartist}'
personal_track_url = f'https://api.spotify.com/v1/me/top/tracks?limit={limitsong}'



artists = ''
response = requests.get(personal_artist_url, headers={"Content-Type":"application/json","Authorization": f"Bearer {access_token}"})
print(response)

count = 0

for i in response.json().get("items"):
    artists+=(str(i.get("id")))
    if count != limitartist-1:
        artists += ","
        count+=1
print(artists)

songs = ''
response = requests.get(personal_track_url, headers={"Content-Type":"application/json","Authorization": f"Bearer {access_token}"})
print(response)

count = 0

for i in response.json().get("items"):
    songs+=(str(i.get("id")))
    if count != limitsong-1:
        songs+=","
        count+=1

print(songs)



# FILTERS
limit = 10  # no. of songs
market = "AU"  # country
seed_genres = "indie,psych-rock"
# ID for Hippo Campus, Glass Animals, San Cisco
seed_artists = "1btWGBz4Uu1HozTwb2Lm8A,4yvcSjfu4PC0CYQyLy4wSq,0Ou0138wEd8XWebhc4j7O0"
energy = 0.6
valence = 0.8
seed_artists = artists
seed_tracks = songs
uris = []
query = f'{endpoint_url}limit={limit}&market={market}&seed_genres={seed_genres}&energy={energy}&seed_artists={seed_artists}&valence={valence}'

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
          "name": "Popular Artists by python",
          "description": "Magic",
          "public": False
        })
response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {access_token}"})

url = response.json()['external_urls']['spotify']
print(response.status_code)


#ADD SONGS TO NEW PLAYLIST
playlist_id = response.json()['id']

endpoint_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

request_body = json.dumps({
          "uris" : uris
        })
response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {access_token}"})

print(response.status_code)

print(f'Your playlist is ready at {url}')


