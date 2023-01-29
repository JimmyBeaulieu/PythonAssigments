# use random to produce two positive one-digit integers. the program should
# then prompt the user with a question, such as:
import random


# how much is 6(first random one-digit integer) times 7(second random one-digit integer)?
# the user then inputs the answer. the program checks the user's answer. if
# it's correct, display the message "very good" and ask another multiplication
# question. if the answer is wrong, display the message "No. try again" and
# let the user try THE SAME QUESTION repeatedly until the user gets it
# right ! a separate method should be used to generate each new question.
# this method should be called once when the app begins execution and each time
# the user answers the question correctly.

def main():
    while True:
        check = False
        answer = questionAsker()
        while not check:
            userinput = int(input())
            if userinput != answer:
                print("No. try again")
            if userinput == answer:
                print("very good")
                check = True


def questionAsker():
    num1 = random.randrange(1, 9)
    num2 = random.randrange(1, 9)
    print("how much is ", num1, " times ", num2, " ?")
    return num1 * num2


main()
