from datetime import date, timedelta, time


# 1 Complete read_date()
def read_date():
    """Read a string representing a date in the format 2121-04-12, create a
    date object from the input string, and return the date object
    """
    date_str = input()
    year, month, day = date_str.split('-')
    return date(int(year), int(month), int(day))
    


# 2. Use read_date() to read four (unique) date objects, putting the date objects in a list
listofdates = []
for i in range(4):
    listofdates.append(read_date())
# 3. Use sorted() to sort the dates, earliest first
sortedDates = sorted(listofdates)
# 4. Output the sorted_dates in order, earliest first, in the format mm/dd/yy
for d in sortedDates:
    print(d.strftime('%m/%d/%Y'))
# 5. Output the number of days between the last two dates in the sorted list
#    as a positive number
print((sortedDates[3] - sortedDates[2]).days)
# 6. Output the date that is 3 weeks from the most recent date in the list
print((max(sortedDates) + timedelta(weeks=3)).strftime('%B %d, %Y'))
# 7. Output the full name of the day of the week of the earliest day
print(min(sortedDates).strftime('%A'))