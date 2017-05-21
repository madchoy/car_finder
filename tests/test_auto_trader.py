from _decimal import Decimal

import pkg_resources

from car_finder.auto_trader import AutoTrader


def load_file(filename):
    return pkg_resources.resource_stream(__name__, f"/data/{filename}")


class TestAutoTrader(object):
    def test_parse_car(self):
        trader = AutoTrader()
        car_listing = load_file('sample_accord.html')
        car = trader.parse_car(car_listing)
        assert Decimal('92291') == car.kilometers
