# Develop an algorithm that determines the greater value out of two numbers provided by the user. Display this value.
first = float(input("First number: "))
second = float(input("Second number: "))
if first < second :
    print(str(second) + " is bigger than " + str(first))
else:
    print(str(first) + " is bigger than " + str(second))
