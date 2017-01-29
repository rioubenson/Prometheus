import inspect

import pandas as pd

from prometheus.core.apollo import Security
from prometheus.core.inspect import isproperty


class Position(object):
    """
        A Position object that models one position within a portfolio
    """

    def __init__(self, symbol, exchange, units):
        self.symbol = symbol
        self.product = Security(symbol, 'EquityIndexFuture', 1000) # Pull from Apollo
        self.exchange = exchange
        self.units = units

    @property
    def market_value(self):
        return self.units * self.product.multiplier * self.product.current_market_price

    def as_series(self):
        """
            Returns the position as a Series
        :return: A Pandas Series
        """
        labels = []
        data = []
        for v in vars(self):
            labels.append(v)
            data.append(getattr(self, v))
        # Now loop over propeties
        for (d, v) in inspect.getmembers(Position, isproperty):
            labels.append(d)
            data.append(getattr(self,d))
        return pd.Series(data,index=labels)
