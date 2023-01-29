# Give an algorithm that reads three numbers (a, b, c) and determines whether any one of the numbers
# is equal to the sum of the other two. If such a number exists, display it;
# otherwise, display the message “No solution”.

a = int(input("Please enter number a:"))
b = int(input("Please enter number b:"))
c = int(input("Please enter number c:"))

if a == (b+c):
    print("a is equal to the sum of b+c")
if b == (a+c):
    print("b is equal to the sum of a+c")
if c == (a+b):
    print("c is equal to the sum of a+b")
else:
    print("No solution")