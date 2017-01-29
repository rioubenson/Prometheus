"""A temp holding class that will be replaced with the Apollo Module"""

class Security(object):
    def __init__(self, symbol, type, multiplier):
        self.symbol = symbol
        self.type = type
        self.multiplier = multiplier

    @property
    def current_market_price(self):
        return 1.5 # To get from Apollo
