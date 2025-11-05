#cd Repository Checkpoint 11
#api.py

import requests
import json

song = input("What song are you looking for?")

response = requests.get("https://itunes.apple.com/search?entity=song&limit=20&term="+song)
#print(json.dumps(response.json(), indent=2))
search = response.json()
for result in search["results"]:
    print(result["trackName"], result["artistName"])

print("-" * 45)

city = input("City: ")
response2 = requests.get("http://goweather.xyz/weather/"+city)
search2 = response2.json()
# for result in search2["results"]:
print(search2["temperature"], search2["wind"])
print(response2.json())