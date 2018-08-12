from helpers.distance import Calculator

from settings import API_KEY


class Newz(object):
    def __init__(self):
        pass

    def run(self):
        origins = 'Kubanska 2 Brno'
        destinations = 'Palachovo namesti 4 Brno'

        print('There is something here, yay.')
        calc = Calculator(api_key=API_KEY)
        result = calc.get_distance(origins=origins, destinations=destinations)
        print(result)

