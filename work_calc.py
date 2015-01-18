#!/usr/bin/env python
# encoding: utf-8

from datetime import date
from workalendar.usa import Tennessee

PRIME_DATE = date(2014, 12, 1)
DAY_DICT = {
    1: "First day of days",
    2: "Second day of days",
    3: "Third day of days",
    4: "Fourth day of days",
    5: "First day of long break",
    6: "Second day of long break",
    7: "Third day of long break",
    8: "Fourth day of long break",
    9: "Fifth day of long break",
    10: "Sixth day of long break",
    11: "First night of nights (thurs)",
    12: "Second night of nights (fri)",
    13: "Third night of nights (sat)",
    14: "Fourth night of nights (sun)",
    15: "First day off between nights and hell week",
    16: "Second day off between nights and hell week",
    17: "Third day off between nights and hell week",
    18: "Last day off between nights and hell week",
    19: "First day of hell week",
    20: "Second day of hell week",
    21: "Third day of hell week",
    22: "First night of hell week (mon)",
    23: "Second night of hell week (tues)",
    24: "Third night of hell week (wed)",
    25: "First day off between hell week and training",
    26: "Second day off between hell week and training",
    27: "Third day off between hell week and training",
    28: "Last day off between hell week and training",
    29: "First day of training",
    30: "Second day of training",
    31: "Third day of training",
    32: "Fourth day of training",
    33: "Fifth day of training",
    34: "First day off between training and days",
    35: "Second day off between training and days",
}
cal = Tennessee()
holidays = cal.holidays(2015)
test = dict(holidays)
holiday_dates = []
for i in range(0, len(holidays)):
    holiday_dates.append(holidays[i][0])


def get_date():
    try:
        year = int((input("Please enter the year: ")) or date.today().year)

        month = int((input("Please enter the month: ")) or date.today().month)
        while month not in range(1, 13):
            print("That is not a valid month.")
            month = int(input("Please enter the month: ") or date.today().month)

        day = int((input("Please enter the day: ") or date.today().day))
        if month in (1, 3, 5, 7, 8, 10, 12):
            while day not in range(1, 32):
                print(
                    "That is not a valid day. Please enter a number from 1-31: ")
                day = int((input("Please enter the day: ")) or date.today().day)
        elif month in (4, 6, 9, 11):
            while day not in range(1, 31):
                print(
                    "That is not a valid day. Please enter a number from 1-30: ")
                day = int((input("Please enter the day: ")) or date.today().day)
        elif month == 2 and year % 4 != 0:  # not a leap year
            while day not in range(1, 29):
                print(
                    "That is not a valid day. Please enter a number from 1-28: ")
                day = int((input("Please enter the day: ")) or date.today().day)
        elif month == 2 and year % 4 == 0:  # leap year
            while day not in range(1, 30):
                print(
                    "That is not a valid day. Please enter a number from 1-29: ")
                day = int((input("Please enter the day: ")) or date.today().day)
        return date(year, month, day)
    except ValueError:
        print("That is an unacceptable error. I quit!")
        exit()


req_date = get_date()

print("\n\n" + req_date.strftime("%x") + "\n" +
      DAY_DICT[(req_date.toordinal() - PRIME_DATE.toordinal()) % 35 + 1])
if req_date in test:
    print("\nAlso, that day is {0}!".format(test[req_date]))
