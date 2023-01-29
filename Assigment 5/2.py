# Given an integer array of digits, return the largest multiple of three that can be
# formed by concatenating some given digits in any order.
# Since the answer may not fit in an integer data type, return the answer as a string.
# If there is no answer return an empty string.
#
# Example 1:
# Input: digits = [8,1,9]
# Output: "981"

userInput = input("Please enter a number: ")
total = 0
result = ""
userInputSplit = []

for number in userInput:
    userInputSplit.append(number)

for number in userInputSplit:
    total += int(number)

if total % 3 == 0:
    userInputSplit.sort(reverse=True)
    for number in userInputSplit:
        result += str(number)

    print("The biggest multiple of three that can be formed with your given digit is: " + result)
else:
    print("Your number is not a multiple of three")
