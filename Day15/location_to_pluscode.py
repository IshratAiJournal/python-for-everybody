import urllib.request
import urllib.parse
import json
from openlocationcode import openlocationcode as olc  # ✅ CORRECT WAY

serviceurl = "http://py4e-data.dr-chuck.net/opengeo?"

while True:
    address = input("Enter location: ")
    if len(address) < 1:
        break

    url = serviceurl + urllib.parse.urlencode({'q': address})
    print("Retrieving", url)

    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'features' not in js or len(js['features']) == 0:
        print("==== Failure To Retrieve ====")
        continue

    lat = js['features'][0]['geometry']['coordinates'][1]
    lng = js['features'][0]['geometry']['coordinates'][0]
    print("Latitude:", lat)
    print("Longitude:", lng)

    plus_code = olc.encode(lat, lng)  # ✅ NOW THIS WILL WORK
    print("Plus Code:", plus_code)
