import readtime


class Reader(object):

    def __init__(self):
        pass

    def get_readtime(self, input_text):
        result_time = readtime.of_text(input_text).minutes
        return result_time
