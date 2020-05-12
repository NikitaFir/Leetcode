from datetime import datetime

class Solution(object):
    def dayOfTheWeek(self, day, month, year):

        if len(str(day)) == 1:
            day = "0" + str(day)
        if len(str(month)) == 1:
            month = "0" + str(month)

        data = str(day) + str(month) + str(year)

        currentday = datetime.strptime(data, '%d%m%Y')

        days_of_week = {1 : "Monday", 2 : "Tuesday", 3 : "Wednesday", 4 : "Thursday", 5 : "Friday", 6 : "Saturday", 7 : "Sunday"}

        return days_of_week.get(currentday.isoweekday())

print(Solution.dayOfTheWeek(0, 31, 8, 2019))
print(Solution.dayOfTheWeek(0, 18, 7, 1999))
print(Solution.dayOfTheWeek(0, 15, 8, 1993))
print(Solution.dayOfTheWeek(0, 25, 1, 2013))
print(Solution.dayOfTheWeek(0, 3, 12, 1992))