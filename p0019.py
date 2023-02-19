# Copyright 2023, Dustin Keate, All rights reserved.

# Counting Sundays

# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?



# DATES ARE DUMB, THIS IS WHY EVERY LANGUAGE HAS A DATE CLASS

thirty_days = [4,6,9,11]
thirtyone_days = [1,3,5,7,8,10,12]

day = 6
month = 1
year = 1

first_sundays = 0

while year <= 100:
  day += 7
  if month == 2 and day >= 28:
    if year % 4 == 0:
      # ignore centuries because 1901 to 2000 is not a problem
      if day >= 29:
        day -= 29
        month += 1
    else:
      day -= 28
      month += 1
  elif day >= 31 and month in thirtyone_days:
    day -= 31
    month += 1
    if month > 12:
      month -= 12
      year += 1
  elif day >= 30 and month in thirty_days:
    day -= 30
    month += 1

  if day == 1:
    first_sundays += 1
  
  print (f"{day}/{month}/{year}")

print(first_sundays)
