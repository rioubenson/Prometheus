import unittest

from prometheus.position.position import Position


class TestPosition(unittest.TestCase):
    def test_as_series(self):
        p = Position('FESX032017', 'EUREX', 100)
        self.assertEqual(p.as_series()['units'], 100, "Did not get expected units")

    def test_market_value(self):
        p = Position('FESX032017', 'EUREX', 100)
        self.assertEqual(p.market_value, 150000, "Market Value Incorrect, got %s" % p.market_value)


if __name__ == '__main__':
    unittest.main()
