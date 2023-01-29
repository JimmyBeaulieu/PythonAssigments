# Write an algorithm that reads a positive integer ( > 0 ) and determines whether it is a prime number.
# (Hint: try dividing the number by the numbers coming before it.)
# Validate the input.

# while loop

num = int(input("Enter a number: "))
isPrime = False
if num > 0:
    i = 2
    while i < num:
        if (num % i) == 0:
            isPrime = True
            break
        i = i+1
if isPrime:
    print(str(num) + " is not a prime number")
else:
    print(str(num) + " is a prime number")
