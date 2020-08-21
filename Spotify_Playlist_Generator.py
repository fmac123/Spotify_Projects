import requests
import json

# SETTINGS 
endpoint_url = "https://api.spotify.com/v1/recommendations?"
#This isn't permanent probably need to reget token???
token = "BQABbuPO2sDoJNs9IJ_HK5SCGQ7_tVhRk_1XYQMcpC5X7e9mPu6d3mcR4s3R2Rm-QkobINtOCcxCOlHgJAOq9Jx8v-LT-dPBp2uyvRq3YOAnPU9r-Wo3WkHQEvO-oUOE4H0BIGalrazeX3c3wuJKVXYYMgTlhl5srFq_wc5mCY8G4A"
user_id = "rhythm_20"

# OUR FILTERS
limit=10
market="US"
seed_genres="indie"
danceability=0.6
uris = [] 
seed_artists = '1btWGBz4Uu1HozTwb2Lm8A', '4yvcSjfu4PC0CYQyLy4wSq','0Ou0138wEd8XWebhc4j7O0'  # ID for Hippo Campus, Glass Animals and San Cisco
#seed_tracks = '5VGEgFZfWBoEOGb3Vlo3rU'  # ID for Tangerine by Glass Animals

# PERFORM THE QUERY
query = f'{endpoint_url}limit={limit}&market={market}&seed_genres={seed_genres}&danceability={danceability}'
query += f'&seed_artists={seed_artists}'
query += f'&seed_tracks={seed_tracks}'

response = requests.get(query, 
               headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {token}"})
json_response = response.json()

print('Recommended Songs:')
for i,j in enumerate(json_response['tracks']):
            uris.append(j['uri'])
            print(f"{i+1}) \"{j['name']}\" by {j['artists'][0]['name']}")

# CREATE A NEW PLAYLIST

endpoint_url = f"https://api.spotify.com/v1/users/{user_id}/playlists"

request_body = json.dumps({
          "name": "Indie bands like Hippo Campus and Glass Animals but using Python",
          "description": "My first programmatic playlist, yooo!",
          "public": False
        })
response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {token}"})

url = response.json()['external_urls']['spotify']
print(response.status_code)


# FILL THE NEW PLAYLIST WITH THE RECOMMENDATIONS

playlist_id = response.json()['id']

endpoint_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

request_body = json.dumps({
          "uris" : uris
        })
response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {token}"})

print(response.status_code)

print(f'Your playlist is ready at {url}')

