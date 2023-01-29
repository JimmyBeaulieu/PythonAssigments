# Write a program that receives three integers entered via the keyboard, and that displays
# the sum,
# the average,
# the product,
# the smallest,
# and the largest of these numbers.

numbers = [int(input("Please enter your first number: ")), int(input("Please enter your second number: ")),
           int(input("Please enter your third number: "))]

total = numbers[0] + numbers[1] + numbers[2]

print("the sum of all the numbers is: " + str(total))
print("the average of all the numbers is: " + str(total/3))
print("The product of all the numbers is: " + str(numbers[0] * numbers[1] * numbers[2]))
print("The smallest value is : " + str(min(numbers)))
print("The biggest value is : " + str(max(numbers)))
