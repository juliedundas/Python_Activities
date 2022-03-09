#Import dependencies
import requests

#Link to Spotify API
response = requests.get("https://developer.spotify.com/")

#Print the response to ensure a successful connection. Response 200 indicates a successful connection
print(response)  

