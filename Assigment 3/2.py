# Imagine a relation between 2 numbers in such :
# the sum of factors including 1 (but not the number itself) of one number
# is equal to the other number and vice versa.
# for example, (220,284) have such a relation. the factors of 220 are
# 1,2,4,5,10,11,20,22,44,55, and 110 whose sum equals 284. the factors of 284
# are 1,2,4,71,142 whose sum equals 220.
# Write a function checkRelation which you call from main() and checks
# whether a pair of numbers entered has this relation or has not. Display
# the factors of each number to confirm your answer.

def main():
    checkRelation(220, 284)


def checkRelation(first, second):
    firstArray = []
    secondArray = []

    firstSum = 0
    secondSum = 0

    for i in range(1, first + 1):
        if i == first:
            i = first + 1
        if first % i == 0:
            firstArray += [i]

    for i in range(1, second + 1):
        if i == second:
            i = second + 1
        if second % i == 0:
            secondArray += [i]

    i = 0
    while i < len(firstArray):
        firstSum += firstArray[i]
        i += 1

    i = 0
    while i < len(secondArray):
        secondSum += secondArray[i]
        i += 1

    if firstSum == second and secondSum == first:
        print("There is a relation between both numbers!")
    else:
        print("there is no such thing as a relation between them two!")


main()
