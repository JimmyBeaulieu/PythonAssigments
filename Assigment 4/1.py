# This challenge is about using a collection (list) of integers and allowing the user
# to select options from a menu to perform operations on the list.
#
# Your program should display a menu options to the user as follows:
#
# P - Print numbers
# A - Add a number
# M - Display mean of the numbers
# S - Display the smallest number
# L - Display the largest number
# Q - Quit
#
# Enter your choice:
#
# The program should only accept valid choices from the user, both upper and lowercase selections should be allowed.
# If an illegal choice is made, you should display, "Unknown selection, please try again" and
# the menu options should be displayed again.
#
# If the user enters 'P' or 'p', you should display all the elements (ints) in the list.
# If the list is empty you should display "[] - the list is empty"
# If the list is not empty then all the list element should be displayed inside square brackets separated by a space.
# For example, [ 1 2 3 4 5 ]
#
# If the user enters 'A' or 'a' then you should prompt the user for an integer to add to the list
# which you will add to the list and then display it was added. For example, if the user enters 5
# You should display, "5 added".
# Duplicate list entries are OK ! (for now. check a bit further for added functionalities…)
#
# If the user enters 'M' or 'm'  you should calculate the mean or average of the elements in the list and display it.
# If the list is empty you should display, "Unable to calculate the mean - no data"
#
# If the user enters 'S' or 's' you should display the smallest element in the list.
# For example, if the list contains [2 4 5 1],  you should display, "The smallest number is 1"
# If the list is empty you should display, "Unable to determine the smallest number - list is empty"
#
# If the user enters 'L' or 'l' you should display the largest element in the list
# For example, if the list contains [2 4 5 1], you should display, "The largest number is 5"
# If the list is empty you should display, "Unable to determine the largest number - list is empty"
#
# If the user enters 'Q' or 'q' then you should display 'Goodbye" and the program should terminate.
#
# Before you begin. Write out the steps you need to take and decide in what order they should be done. PSEUDOCODE
# Think about what loops you should use as well as what you will use for your selection logic.
#
# Finally, be sure to test your program as you go and at the end.
#
# Hint: Use a List!
#
# Additional functionality:
#
# - search for a number in the list and if found display the number of times it occurs in the list
# - clearing out the list (make it empty again) (Hint: the vector class has a .clear() method)
# - don't allow duplicate entries
# - come up with your own ideas! (add up one more functionality. Be creative !!)
import random


def Display(array):
    i = 0
    tempList = ""
    if len(array) == 0:
        print("\n[] - the list is empty\n")
    else:
        while i < len(array):
            tempList += str(array[i]) + " "
            i += 1
        print("\n[ " + tempList + "]\n")


def Adder(array):
    num = int(input("\nPlease enter an integer: "))
    if num < 0 or num > 0 or num == 0:
        array.append(num)
        print("\n" + str(num) + " was added!\n")
    else:
        print("\nInvalid, please enter an integer only\n")


def Average(array):
    total = 0
    if len(array) <= 0:
        print("\nUnable to calculate the mean - no data\n")
    else:
        for i in array:
            total += i
        print("\nThe average is: " + str(total / len(array)) + "\n")


theList = []

while True:
    userInput = str(input("P - Print numbers\n"
                          "A - Add a number\n"
                          "M - Display mean of the numbers\n"
                          "S - Display the smallest number\n"
                          "L - Display the largest number\n"
                          "Q - Quit\n\n"
                          "Enter your choice: "))
    # print(userInput)
    if userInput == "debug":
        i = 0
        while i < 30:
            theList.append(random.randrange(0, 100))
            i += 1

    if userInput == "p" or userInput == "P" or userInput == "a" or userInput == "A" or userInput == "m"\
            or userInput == "M" or userInput == "s" or userInput == "S" or userInput == "l" or userInput == "L"\
            or userInput == "q" or userInput == "Q":
        if userInput == "p" or userInput == "P":
            Display(theList)
        if userInput == "a" or userInput == "A":
            Adder(theList)
        if userInput == "m" or userInput == "M":
            Average(theList)
        if userInput == "s" or userInput == "S":
            if len(theList) <= 0:
                print("\nUnable to determine the smallest number - list is empty!\n")
            else:
                print("\nThe smallest number is: " + str(min(theList)) + "\n")

        if userInput == "l" or userInput == "L":
            if len(theList) <= 0:
                print("\nUnable to determine the biggest number - list is empty!\n")
            else:
                print("\nThe biggest number is: " + str(max(theList)) + "\n")

        if userInput == "q" or userInput == "Q":
            quit(0)
    else:
        print("\nUnknown selection, please try again.\n")
