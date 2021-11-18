# -*- coding: utf-8 -*-


from calendar import isleap


# judge the leap year
def judge_leap_year(year):
    if isinstance(year, int) and year > 0:
        if isleap(year):
            return True
        else:
            return False
    else:
        return 'Failed! Invalid value'


# returns the number of days in each month
def month_days(month, leap_year):
    if isinstance(month, int) and isinstance(leap_year, bool):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2 and leap_year:
            return 29
        elif month == 2 and (not leap_year):
            return 28
    else:
        return 'Failed! Invalid value'
