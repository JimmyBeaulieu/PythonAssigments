# Write a program that asks the user to enter two numbers, and that displays the sum, the product,
# the difference, and the quotient of these two numbers.

num1 = int(input("Please enter the first number: "))
num2 = 0
while num2 == 0:
    num2 = int(input("Please enter the second number: "))
    if num2 == 0:
        print("Please do not put 0 as second value ")

print(str(num1) + " + " + str(num2) + " = " + str(num1 + num2))
print(str(num1) + " - " + str(num2) + " = " + str(num1 - num2))
print(str(num1) + " * " + str(num2) + " = " + str(num1 * num2))
print(str(num1) + " / " + str(num2) + " = " + str(num1 / num2))
