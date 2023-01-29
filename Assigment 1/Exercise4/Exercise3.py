# Write a program that reads three values and displays them in ascending order.
check = True
while check:
    try:
        a = int(input("Please enter your first number: "))
        b = int(input("Please enter your second number: "))
        c = int(input("Please enter your third number: "))
        check = False
    except:
        print("Invalid value, please only write an integer number.")

numbers = [a,b,c]

###################################################- easy version -####################################################

print(str(max(numbers)) + " is the greatest number.")

###################################################- cool version -####################################################

largest = numbers[0]
for x in numbers:
    if x > largest:
        largest = x

print(str(largest) + " is the greatest number.")
