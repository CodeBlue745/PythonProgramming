import calendar, datetime

# Complete the function to print the full name of the day of the week
def printWeekdayName(year, month, day):
    print(calendar.day_name[datetime.date(year,month,day).weekday()])
# Student code goes here
 
# expected output: Friday    
printWeekdayName(2001, 8, 31)
 
# expected output: Monday
printWeekdayName(2018, 10, 1)