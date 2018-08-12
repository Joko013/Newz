from helpers.distance import Calculator

from settings import API_KEY


class Newz(object):
    def __init__(self):
        self.calculator = Calculator(api_key=API_KEY)

    def run(self):
        origins = 'Kubanska 2 Brno'
        destinations = 'Palachovo namesti 4 Brno'

        self.result = self.calculator.get_distance(origins=origins, destinations=destinations)

        print('The route will take {0} minutes.'.format(self.result))

