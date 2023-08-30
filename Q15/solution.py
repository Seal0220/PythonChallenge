# http://www.pythonchallenge.com/pc/return/uzi.html

import calendar

'''
'Monday': 0,
'Tuesday': 1,
'Wednesday': 2,
'Thursday': 3,
'Friday': 4,
'Saturday': 5,
'Sunday': 6
'''       

month, day, weekday = 1, 26, 0
years = []
for year in range(1016, 1996+1, 20):
    if calendar.weekday(year, month, day) == weekday:
        years.append(year)

print(years) # [1176, 1356, 1576, 1756, 1976]
