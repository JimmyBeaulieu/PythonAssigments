# Create an algorithm that determines whether a year provided by the user is a leap year.
# To be a leap year, a year must be divisible by 4 but not divisible by 100;
# despite this, if it is divisible by 400, it is a leap year after all.
# Example: 2000 is a leap year, but 1700, 1800, and 1900 are not.

year = int(input("Please enter a year: "))
isLeapYear = False
if year % 100 != 0 and year % 4 == 0:
    isLeapYear = True
if year % 400 == 0:
    isLeapYear = True
if isLeapYear:
    print(str(year) + " is a leap year.")
else:
    print(str(year) + " is not a leap year.")
