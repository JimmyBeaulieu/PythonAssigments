# Write a program that asks the user to enter two integers, and that displays the larger number,
# followed by the words “ is greater than ”, followed by the smaller number.
# However, if the numbers are equal, the program should display “These numbers are equal.”

num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter the second number: "))

if num1 > num2:
    print(str(num1) + " is bigger than " + str(num2))
if num1 < num2:
    print(str(num2) + " is bigger than " + str(num1))
if num1 == num2:
    print(str(num1) + " is equal to " + str(num2))
