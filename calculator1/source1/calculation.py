import time


class Calculation:
    def __init__(self, raw):
        self.raw = raw
        self.timestamp = int(round(time.time() * 1000))