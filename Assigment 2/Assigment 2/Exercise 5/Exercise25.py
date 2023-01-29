# Write an algorithm that reads two triplets day1, month1, year1, and day2, month2, year2, representing two dates,
# and that determines whether the first date comes before the second.

year1 = int(input("Enter the first year : "))
month1 = int(input("Enter the first month : "))
day1 = int(input("Enter the first day : "))
year2 = int(input("Enter the second year : "))
month2 = int(input("Enter the second month : "))
day2 = int(input("Enter the second day : "))

if year1 > year2:
    print(str(day1) +"/"+ str(month1) +"/"+ str(year1) + " (day1-month1-year1) is the farthest date in time")
if year2 > year1:
    print(str(day2) +"/"+ str(month2) +"/"+ str(year2) + " (day2-month2-year2) is the farthest date in time")
else:
    if month1 > month2:
        print(str(day1) +"/"+ str(month1) +"/"+ str(year1) + " (day1-month1-year1) is the farthest date in time")
    if month2 > month1:
        print(str(day2) +"/"+ str(month2) +"/"+ str(year2) + " (day2-month2-year2) is the farthest date in time")
    else:
        if day1 > day2:
            print(str(day1) +"/"+ str(month1) +"/"+ str(year1) + " (day1-month1-year1) is the farthest date in time")
        if day2 > day1:
            print(str(day2) +"/"+ str(month2) +"/"+ str(year2) + " (day2-month2-year2) is the farthest date in time")
