class Portfolio(object):
    """
        A portfolio object that contains 1 or more books
    """

    def __init__(self, strategy, on_date, label, books):
        self.strategy = strategy
        self.date = on_date
        self.label = label
        self.books = books

    @property
    def market_value(self):
        mv = 0
        for b in self.books:
            mv += b.market_value
        return mv

    

