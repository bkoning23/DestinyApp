import requests
import pprint
import json

url = "http://www.bungie.net/Platform/Destiny/SearchDestinyPlayer/2/Cookieking232"

API_KEY = "5e78813d2af641428d781d921ad9a1c2"

headers = {"X-API-KEY": API_KEY}

#url = "http://www.bungie.net/Platform/Destiny/2/Account/

r = requests.get(url, headers=headers)
print(r.json())
print(type(r))

r = r.json()

id = r["Response"][0]["membershipId"]
print(id)

url = "http://www.bungie.net/Platform/Destiny/2/Account/" + id

r = requests.get(url, headers=headers)
charId = r.json()["Response"]["data"]["characters"][0]["characterBase"]["characterId"]



print(charId)

url = "http://www.bungie.net/Platform/Destiny/Stats/ActivityHistory/2/" + id + "/" + charId + "/?mode=Raid"
r = requests.get(url, headers=headers)
print(url)
print(json.dumps(r.json(), indent = 4, sort_keys=True))

