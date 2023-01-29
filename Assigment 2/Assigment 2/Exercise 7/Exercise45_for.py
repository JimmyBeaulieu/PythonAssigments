# Write an algorithm that displays the first 100 numbers of the Fibonacci sequence.
# This sequence begins with the numbers 1, 1, 2, 3, 5, 8, …,
# where each new number in the sequence can be found by adding the two previous numbers in the sequence.

# for loop

displayedNumber = 1
firstNumber = 1
secondNumber = 0
print(0)
for i in range(0, 100):
    print(displayedNumber)
    displayedNumber = firstNumber + secondNumber
    secondNumber = firstNumber
    firstNumber = displayedNumber
