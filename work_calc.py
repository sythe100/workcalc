#!/usr/bin/env python
# encoding: utf-8

from datetime import date, datetime
from workalendar.usa import Tennessee
from config import PRIME_DATE, DAY_DICT

cal = Tennessee()


def get_date():
    try:
        inp_date = input("Please enter the date in MM-DD-YY format: ")
        inp_date = datetime.strptime(inp_date, "%m-%d-%y")
    except ValueError:
        print("That is not a valid date.")
        exit()

    return inp_date

req_date = datetime.date(get_date())
holidays = dict(cal.holidays(req_date.year))

print("\n\n" + req_date.strftime("%x") + "\n" +
      DAY_DICT[(req_date.toordinal() - PRIME_DATE.toordinal()) % 35 + 1])
if req_date in holidays:
    print("\nAlso, that day is {0}!".format(holidays[req_date]))
