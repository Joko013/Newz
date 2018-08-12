from datetime import datetime

import googlemaps


class Calculator(object):
    def __init__(self, api_key):
        self.client = googlemaps.Client(api_key)
        self.departure_time = datetime.now()

    @staticmethod
    def get_distance_min(distance_sec):
        distance_min = distance_sec / 60
        return distance_min

    def get_distance(self, origins, destinations,
                     mode='transit'):

        distance_matrix = self.client.distance_matrix(origins=origins, destinations=destinations,
                                                      mode=mode, departure_time=self.departure_time)

        result_sec = distance_matrix['rows'][0]['elements'][0]['duration']['value']

        return self.get_distance_min(result_sec)
