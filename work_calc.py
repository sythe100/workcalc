#!/usr/bin/env python
# encoding: utf-8

from datetime import date, datetime
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


def get_date():
    try:
        inp_date = input("Please enter the date in MM-DD-YY format: ")
        inp_date = datetime.strptime(inp_date, "%m-%d-%y")
    except ValueError:
        print("That is not a valid date.")
        exit()

    return inp_date

req_date = datetime.date(get_date())

print("\n\n" + req_date.strftime("%x") + "\n" +
      DAY_DICT[(req_date.toordinal() - PRIME_DATE.toordinal()) % 35 + 1])
if req_date in test:
    print("\nAlso, that day is {0}!".format(test[req_date]))
