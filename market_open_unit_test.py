import unittest
import market_open as mo

class MarketOpen(unittest.TestCase):

    def test_weekend(self):
        self.assertTrue(mo.MarketOpen('2021-05-07').market_open)  # works for weekday
        self.assertFalse(mo.MarketOpen('2021-05-09').market_open)  # works for weekend

    def test_new_years(self):
        self.assertFalse(mo.MarketOpen('2021-01-01').market_open)
        self.assertFalse(mo.MarketOpen('2022-01-01') .market_open)  # Saturday Jan 1
        self.assertFalse(mo.MarketOpen('2022-01-02')  .market_open)  # Monday Jan 2 is off
        self.assertTrue(mo.MarketOpen('2021-12-31') .market_open)  # Friday Dec 31 is trading day

    def test_mlk_day(self):
        self.assertFalse(mo.MarketOpen('2021-01-18')  .market_open)  # MLK day 2021
        self.assertTrue(mo.MarketOpen('2021-01-19').market_open)  # Day after MLK day 2021
        self.assertFalse(mo.MarketOpen('2022-01-17').market_open)  # MLK Day 2022
        self.assertFalse(mo.MarketOpen('2023-01-16') .market_open)  # MLK Day 2022

    def test_presidents_day(self):
        self.assertFalse(mo.MarketOpen('2021-02-15').market_open)  # Presidents day 2021
        self.assertTrue(mo.MarketOpen('2021-02-16').market_open)  # Day after Presidents day 2021
        self.assertFalse(mo.MarketOpen('2022-02-21').market_open)  # Presidents Day 2022
        self.assertFalse(mo.MarketOpen('2023-02-20') .market_open)  # Presidents Day 2022

    def test_good_friday(self):  # lunar calenders suck
        self.assertFalse(mo.MarketOpen('2021-04-02').market_open)  # Good Friday 2021
        self.assertTrue(mo.MarketOpen('2021-04-01').market_open)  # Day before Good Friday 2021
        self.assertFalse(mo.MarketOpen('2022-04-15').market_open)  # Good Friday 2022
        self.assertFalse(mo.MarketOpen('2023-04-07').market_open)  # Good Friday 2022

    def test_memorial_day(self):
        self.assertFalse(mo.MarketOpen('2021-05-31') .market_open)  # Memorial Day 2021
        self.assertTrue(mo.MarketOpen('2021-06-01').market_open)  # Day before Memorial Day 2021
        self.assertFalse(mo.MarketOpen('2022-05-30').market_open)  # Memorial Day 2022
        self.assertFalse(mo.MarketOpen('2023-05-29').market_open)  # Memorial Day 2022

    def test_independence_day(self):
        self.assertFalse(mo.MarketOpen('2022-07-04').market_open)  # July 4th 2022
        self.assertTrue(mo.MarketOpen('2022-07-05').market_open)  # Day before July 4th 2022
        self.assertFalse(mo.MarketOpen('2021-07-05').market_open)  # July 4th 2021 is a Sunday
        self.assertFalse(mo.MarketOpen('2023-07-04').market_open)  # Memorial Day 2022

    def test_labor_day(self):
        self.assertFalse(mo.MarketOpen('2021-09-06').market_open)  # Labor day 2021
        self.assertTrue(mo.MarketOpen('2021-09-07').market_open)  # Day after Labor day 2021
        self.assertFalse(mo.MarketOpen('2022-09-05') .market_open)  # Labor Day 2022
        self.assertFalse(mo.MarketOpen('2023-09-04').market_open)  # Labor Day 2022

    def test_thanksgiving(self):
        self.assertFalse(mo.MarketOpen('2021-11-25').market_open)  # Thanksgiving Day 2021
        self.assertTrue(mo.MarketOpen('2021-11-26').market_open)  # Day after Thanksgiving 2021
        self.assertFalse(mo.MarketOpen('2022-11-24').market_open)  # Thanksgiving 2022
        self.assertFalse(mo.MarketOpen('2023-11-23').market_open)  # Thanksgiving Day 2022

    def test_christmas(self):
        self.assertFalse(mo.MarketOpen('2021-12-24').market_open)  # Friday the 24th of December 2021
        self.assertFalse(mo.MarketOpen('2022-12-26').market_open)  # Monday the 26th of December 2022
        self.assertFalse(mo.MarketOpen('2023-12-25').market_open)  # Christmas 2022
        self.assertTrue(mo.MarketOpen('2023-12-26').market_open)  # Day after Christmas and a Tuesday


if __name__ == '__main__':
    unittest.main()