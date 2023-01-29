# Write an algorithm that reads an integer and determines whether it is even or odd.

userInput = int(input("Please enter an integer: "))
if userInput % 2 == 1:
    print("The value " + str(userInput) + " is an odd number")
else:
    print("The value " + str(userInput) + " is an even number")