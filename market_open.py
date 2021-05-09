import datetime


class MarketOpen:
    # class that, given an input date, will return if holiday with the method .market_open()
    def __init__(self, input_date):
        # get input date without anything else
        self.input_date = datetime.datetime.strptime(str(input_date), '%Y-%m-%d')
        self.day_month = str(self.input_date.day) + '-' + str(self.input_date.month)  # get day and month
        self.weekday = self.input_date.weekday()  # get weekday
        self.market_open = True  # set market to open and set to false if exception occurs

        function_list = ['is_weekend', 'is_not_new_years', 'is_not_mlk', 'is_not_presidents_day', 'is_not_good_friday',
                         'is_not_memorial_day', 'is_not_independence_day', 'is_not_labor_day', 'is_not_thanksgiving',
                         'is_not_christmas']

        for func in function_list:  # run each function to check if the stock exchange is open
            eval('self.' + func + '()')

    def is_weekend(self):
        if self.weekday in [5, 6]:
            self.market_open = False

    def is_not_christmas(self):
        if self.day_month == '25-12':
            self.market_open = False  # christmas day get some presents
        elif (self.weekday == 0) & (self.day_month == '26-12'):  # Monday the 26th of January
            self.market_open = False
        elif (self.weekday == 4) & (self.day_month == '24-12'):  # Friday the 24th of December
            self.market_open = False

    def is_not_labor_day(self):
        dt = datetime.datetime(self.input_date.year, 9, 1)
        if dt.weekday() == 0:
            delta_time = datetime.timedelta(days=(0 - dt.weekday()))
        else:
            delta_time = datetime.timedelta(days=(7 - dt.weekday()))
        labor_day = dt + delta_time  # get the first Monday of September

        if self.input_date == labor_day:
            self.market_open = False

    def is_not_mlk(self):
        dt = datetime.datetime(self.input_date.year, 1, 1)
        if dt.weekday() == 0:
            delta_time = datetime.timedelta(days=(0 - dt.weekday()))
        else:
            delta_time = datetime.timedelta(days=(7 - dt.weekday()))
        dt = dt + delta_time  # get the first Monday of January
        mlk = dt + datetime.timedelta(days=14)  # get the third Monday of January

        if self.input_date == mlk:
            self.market_open = False

    def is_not_good_friday(self):
        # boo lunar calendars
        good_friday_dates = ['2021-4-2', '2022-4-15', '2023-4-7', '2024-3-29', '2025-4-18', '2026-4-03',
                             '2027-3-26', '2028-4-14', '2029-3-30',  '2030-4-19']

        day = str(self.input_date.year) + '-' + str(self.input_date.month) + '-' + str(self.input_date.day)

        if any(day in dates for dates in good_friday_dates):
            self.market_open = False

    def is_not_independence_day(self):
        if self.day_month == '4-7':
            self.market_open = False  # new years day
        elif (self.weekday == 0) & (self.day_month == '5-7'):  # Monday the 5th of July
            self.market_open = False

    def is_not_memorial_day(self):
        dt = datetime.datetime(self.input_date.year, 6, 1)
        delta_time = datetime.timedelta(days=(dt.weekday()))
        memorial_day = dt - delta_time
        if self.input_date == memorial_day:
            self.market_open = False

    def is_not_new_years(self):
        if self.day_month == '1-1':
            self.market_open = False  # new years day
        elif (self.weekday == 0) & (self.day_month == '1-2'):  # Monday the 2nd of January
            self.market_open = False
        # Surprisingly if New Years is on a Saturday, there is no holiday at all

    def is_not_presidents_day(self):
        dt = datetime.datetime(self.input_date.year, 2, 1)
        if dt.weekday() == 0:
            delta_time = datetime.timedelta(days=(0 - dt.weekday()))
        else:
            delta_time = datetime.timedelta(days=(7 - dt.weekday()))

        presidents_day = dt + delta_time + datetime.timedelta(days=14)  # get the 3rd Monday of February

        if self.input_date == presidents_day:
            self.market_open = False

    def is_not_thanksgiving(self):
        dt = datetime.datetime(self.input_date.year, 11, 1)

        if dt.weekday() == 3:
            delta_time = datetime.timedelta(days=(0 - dt.weekday()))
        else:
            delta_time = datetime.timedelta(days=(3 - dt.weekday()))

        thanksgiving = dt + delta_time + datetime.timedelta(days=21)  # get the fourth Thursday of February

        if self.input_date == thanksgiving:
            self.market_open = False

    def market_open(self):
        return self.market_open