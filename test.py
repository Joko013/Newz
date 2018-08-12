from datetime import datetime

import googlemaps

from settings import API_KEY

gmaps = googlemaps.Client(API_KEY)

now = datetime.now()
directions_result = gmaps.distance_matrix(origins="Kubanska 2 Brno",
                                         destinations="Hlavni nadrazi Brno",
                                         mode="transit",
                                         departure_time=now)

print(directions_result)


