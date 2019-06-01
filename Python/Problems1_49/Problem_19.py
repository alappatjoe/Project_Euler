# Project Euler Problem 19

import datetime

count = 0

for year in range(1901,2001):
    for month in range(1,13):
        date = datetime.datetime(year, month, 1)
        if date.strftime("%A") == "Sunday": count += 1

print(count)
