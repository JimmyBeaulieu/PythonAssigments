# In a competition where scores are given by 6 judges,
# a competitor’s final score is calculated as follows:
# first the highest and the lowest of the initial scores are eliminated,
# and then one takes the average of the other 4 scores.
# You are asked to create a program that reads 6 scores and determines the final score according to this method.
import random

grading = [0, 0, 0, 0, 0, 0]
choice = input("Would you prefer to write the scores yourself or you want it random? (y/n)")
if choice == "y" or choice == "Y":
    print("Randomly assigning scores...")
    i = 0
    while i < 6:
        grading[i] = random.randint(0, 10)
        i = i + 1
else:
    i = 0
    while i < 6:
        grading[i] = int(input("Please enter grade #" + str(i + 1) + ": "))
        i = i + 1
grading.sort()
average = (grading[1] + grading[2] + grading[3] + grading[4]) / 4
for grades in grading:
    print(str(grades))

print("The average is " + str(average))
