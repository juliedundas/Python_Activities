#Import dependencies
import requests
import spotipy
import pandas as pd

#Link to Spotify API
response = requests.get("https://developer.spotify.com/")

#Print the response to ensure a successful connection. Response 200 indicates a successful connection
print(response)  

#Create variables to print
# response1 = response.content() # Return the raw bytes of the data payload
# response2 = response.text() # Return a string representation of the data payload
# response3 = response.json() # This method is convenient when the API returns JSON

#Print variables to see what api is returning
#print(response1)
#print(response2)
#print(response3)


from spotipy.oauth2 import SpotifyClientCredentials

#Define Spotify Credentials
cid = '05b79fde9a6747d59b000b7865567627'
secret = '2ef39b1215934af0844f9aadff2b4f17'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#print(sp)

#Code below collects track ids, track names, artist names, and popularity score.
artist_name = []
track_name = []
popularity = []
track_id = []
for i in range(0,100,50):
    track_results = sp.search(q='year:2021', type='track', limit=50,offset=i)
    for i, t in enumerate(track_results['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])

# print(track_name)    

#Convert data to a data frame so that it is easier to analyze
track_dataframe = pd.DataFrame({'artist_name' : artist_name, 'track_name' : track_name, 'track_id' : track_id, 'popularity' : popularity})
#print(track_dataframe.shape)
df = track_dataframe.head()

print(track_dataframe)

