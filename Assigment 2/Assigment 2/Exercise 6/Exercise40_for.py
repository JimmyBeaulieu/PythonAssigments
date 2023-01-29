# Write a program that reads 1000 numbers and determines the largest and the smallest.
import random

# while loop

numbers = [0]
i = 0
while i < 1001:
    number = random.randrange(0, 1000)
    numbers.append(number)
    i += 1
maxNumber = max(numbers)
minNumber = min(numbers)

print("Max number in list is: " + str(maxNumber))
print("Min number in list is: " + str(minNumber))
