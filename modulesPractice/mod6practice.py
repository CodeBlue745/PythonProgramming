import calendar

# Complete the function to return the number of leap years in the list
def countLeapYears(yearList):
    count = 0
    for year in yearList:
        if calendar.isleap(year):
            count += 1
    return count
# Student code goes here
 
# expected output: 2
print(countLeapYears([2001, 2018, 2020, 2090, 2233, 2176, 2200, 2982]))
 
# expected output: 4
print(countLeapYears([2001, 2018, 2020, 2092, 2204, 2176, 2200, 2982]))