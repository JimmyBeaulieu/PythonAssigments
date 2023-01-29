# Complete numbers 35 to 48 two times: first with a for loop, and then with a while loop.

# Write an algorithm that calculates the sum of all the integers contained (inclusively)
# between two positive integer limits entered by the user. The program reads the smallest limit first.
# Example: the sum of the integers between 5 and 10, inclusively.

# for loop version:
check = True
minValue = 0
maxValue = 0
while check:
    minValue = int(input("Please enter minimum range: "))
    if minValue < 0:
        print("Please enter only a positive number")
    else:
        check = False
while not check:
    maxValue = int(input("Pleas enter the maximum range: "))
    if maxValue < minValue:
        print("Please enter a bigger number than the first number")
    else:
        check = True
value = 0
for i in range(minValue, maxValue + 1):
    value += minValue
    minValue += 1

print(value)
