import unittest
import pandas as pd
from prometheus.portfolio.book import Book
from prometheus.position.position import Position


class TestBook(unittest.TestCase):
    def test_load_positions(self):
        p = Position('FESX032017', 'EUREX', 100)
        pos = [p, p, p, p]
        test_book = Book('test_book')
        test_book.load_positions(pos)
        # We should have 4 positions in a dataframe
        self.assertEqual(type(test_book.positions), pd.DataFrame, "Did not get DataFrame")
        self.assertEqual(len(test_book.positions.index), 4,
                         "Did not get 4 positions, got %s" % len(test_book.positions.index))



if __name__ == '__main__':
    unittest.main()
