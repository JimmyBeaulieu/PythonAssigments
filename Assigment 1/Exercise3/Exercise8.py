# Write an algorithm that reads two integers m and n and determines whether m is a multiple of n.

n = int(input("Please enter the base integer: "))
m = int(input("Please enter an integer to see if that one is a multiple of the previous integer: "))

if n % m == 0:
    print(str(m) + " is a multiple of " + str(n))
else:
    print(str(m) + " is NOT a multiple of " + str(n))