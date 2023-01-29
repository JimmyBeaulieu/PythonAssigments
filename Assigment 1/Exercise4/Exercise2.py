# Write a program that reads 3 values, determines the greatest one, and displays it.
check = True
while check:
    try:
        a = int(input("Please enter your first number: "))
        b = int(input("Please enter your second number: "))
        c = int(input("Please enter your third number: "))
    except:
        print("Invalid value, please only write an integer number.")
check = False
greater = 0

if a > b:
    greater = a
if a > c:
    greater = a
else:
    if b > a:
        greater = b
    if b > c:
        greater = b
    else:
        if c > a:
            greater = c
        if c > b:
            greater = c

print(str(greater) + " is the greatest number")
