from datetime import datetime

import googlemaps


class Calculator(object):
    def __init__(self, api_key):
        self.client = googlemaps.Client(api_key)
        self.departure_time = datetime.now()

    def get_distance(self, origins, destinations,
                     mode='transit'):

        departure_time = self.departure_time
        distance_matrix = self.client.distance_matrix(origins=origins, destinations=destinations,
                                             mode=mode, departure_time=departure_time)

        result_sec = distance_matrix['rows'][0]['elements'][0]['duration']['value']
        result_min = round(result_sec/60)
        return result_min
