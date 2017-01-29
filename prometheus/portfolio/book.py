import pandas as pd


class Book(object):
    """
        A book model which contains positions
    """

    def __init__(self, name):
        self.name = name
        self.positions = pd.DataFrame()

    def load_positions(self, positions):
        """
            Loads the positions into the book
        :param positions: A iterable of positions or DataFrame
        :return: None
        """
        if type(positions) is pd.DataFrame:
            self.positions = positions
        else:
            self.positions = pd.DataFrame([p.as_series() for p in positions])

    @property
    def net_market_value(self):
        """
            Returns the Net Market Value of the Book
        :return: The Net Market Value
        """
        return self.positions['market_value'].sum()

    @property
    def abs_market_value(self):
        """
            Returns the Abs Market Value of the Book
        :return: The Abs Market Value
        """
        return self.positions['abs_market_value'].sum()

