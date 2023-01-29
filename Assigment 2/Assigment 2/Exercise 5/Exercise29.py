# Write the algorithm of a program that reads a date (3 integers: day, month, year)
# and that displays the date of the next day (in numbers).
# Suppose that the year is not a leap year.
check = True
while check:
    day = int(input("Please enter the day:"))
    if day > 31 or day < 1:
        print("Wrong day number")
    else:
        check = False
check = True
while check:
    month = int(input("Please enter the month:"))
    if (month < 1 or month > 12) or (day > 28 and month == 2):
        print("Wrong month number")
    else:
        check = False
year = int(input("Please enter the year:"))

day = day + 1
if ((day == 31 and month == 4) or
        (day == 31 and month == 6) or
        (day == 31 and month == 9) or
        (day == 31 and month == 11)):
    day = 1
    month = month + 1
if (day == 32) or (day > 28 and month == 2):
    day = 1
    month = month + 1
if month == 13:
    month = 1
    year = year + 1
print("The next day is: " + str(day) + "/" + str(month) + "/" + str(year))
