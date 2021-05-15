import datetime
import market_open as mo
import unittest


class MarketOpen(unittest.TestCase):

    def test_weekend(self):
        self.assertTrue(mo.market_open('2021-05-07'))  # works for weekday
        self.assertFalse(mo.market_open('2021-05-09'))  # works for weekend

    def test_new_years(self):
        self.assertFalse(mo.market_open('2021-01-01'))
        self.assertFalse(mo.market_open('2022-01-01'))  # Saturday Jan 1
        self.assertFalse(mo.market_open('2022-01-02'))  # Monday Jan 2 is off
        self.assertTrue(mo.market_open('2021-12-31'))  # Friday Dec 31 is trading day

    def test_mlk_day(self):
        self.assertFalse(mo.market_open('2021-01-18'))  # MLK day 2021
        self.assertTrue(mo.market_open('2021-01-19'))  # Day after MLK day 2021
        self.assertFalse(mo.market_open('2022-01-17'))  # MLK Day 2022
        self.assertFalse(mo.market_open('2023-01-16'))  # MLK Day 2022

    def test_presidents_day(self):
        self.assertFalse(mo.market_open('2021-02-15'))  # Presidents day 2021
        self.assertTrue(mo.market_open('2021-02-16'))  # Day after Presidents day 2021
        self.assertFalse(mo.market_open('2022-02-21'))  # Presidents Day 2022
        self.assertFalse(mo.market_open('2023-02-20'))  # Presidents Day 2022

    def test_good_friday(self):  # lunar calenders suck
        self.assertFalse(mo.market_open('2021-04-02'))  # Good Friday 2021
        self.assertTrue(mo.market_open('2021-04-01'))  # Day before Good Friday 2021
        self.assertFalse(mo.market_open('2022-04-15'))  # Good Friday 2022
        self.assertFalse(mo.market_open('2023-04-07'))  # Good Friday 2022

    def test_memorial_day(self):
        self.assertFalse(mo.market_open('2021-05-31'))  # Memorial Day 2021
        self.assertTrue(mo.market_open('2021-06-01'))  # Day before Memorial Day 2021
        self.assertFalse(mo.market_open('2022-05-30'))  # Memorial Day 2022
        self.assertFalse(mo.market_open('2023-05-29'))  # Memorial Day 2022

    def test_independence_day(self):
        self.assertFalse(mo.market_open('2022-07-04'))  # July 4th 2022
        self.assertTrue(mo.market_open('2022-07-05'))  # Day before July 4th 2022
        self.assertFalse(mo.market_open('2021-07-05'))  # July 4th 2021 is a Sunday
        self.assertFalse(mo.market_open('2023-07-04'))  # Memorial Day 2022

    def test_labor_day(self):
        self.assertFalse(mo.market_open('2021-09-06'))  # Labor day 2021
        self.assertTrue(mo.market_open('2021-09-07'))  # Day after Labor day 2021
        self.assertFalse(mo.market_open('2022-09-05'))  # Labor Day 2022
        self.assertFalse(mo.market_open('2023-09-04'))  # Labor Day 2022

    def test_thanksgiving(self):
        self.assertFalse(mo.market_open('2021-11-25'))  # Thanksgiving Day 2021
        self.assertTrue(mo.market_open('2021-11-26'))  # Day after Thanksgiving 2021
        self.assertFalse(mo.market_open('2022-11-24'))  # Thanksgiving 2022
        self.assertFalse(mo.market_open('2023-11-23'))  # Thanksgiving Day 2022

    def test_christmas(self):
        self.assertFalse(mo.market_open('2021-12-24'))  # Friday the 24th of December 2021
        self.assertFalse(mo.market_open('2022-12-26'))  # Monday the 26th of December 2022
        self.assertFalse(mo.market_open('2023-12-25'))  # Christmas 2022
        self.assertTrue(mo.market_open('2023-12-26'))  # Day after Christmas and a Tuesday
        
    def test_dates(self):
        self.assertTrue(mo.market_open('2021-05-07'))  # check again for normal market open date
        self.assertTrue(mo.market_open('2021-5-7'))  # check for dates without 0s
        self.assertTrue(mo.market_open(datetime.date(2021, 5, 7)))  # Check for datetime date
        self.assertTrue(mo.market_open(datetime.datetime(2021, 5, 7, 10, 23)))  # Check for datetime date
        # Check for datetime date, may change if you run on weekend
        #self.assertTrue(mo.market_open(datetime.datetime.now()))

    def test_next_open_day(self):
        self.assertEqual(mo.next_market_open_date('2021-05-13'), '2021-05-14')  # check for Friday
        self.assertEqual(mo.next_market_open_date('2021-05-14'), '2021-05-17')  # check for Weekend
        self.assertEqual(mo.next_market_open_date('2021-05-15'), '2021-05-17')  # check for day on weekend
        self.assertEqual(mo.next_market_open_date('2021-01-15'), '2021-01-19')  # check for MLK
        self.assertEqual(mo.next_market_open_date('2021-11-24'), '2021-11-26')  # check for Thanksgiving


if __name__ == '__main__':
    unittest.main()
