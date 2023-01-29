# Write an algorithm that reads a positive integer ( > 0 ) and determines whether it is a prime number.
# (Hint: try dividing the number by the numbers coming before it.)
# Validate the input.

# for loop

num = int(input("Enter a number: "))
isPrime = False
if num > 0:
    for i in range(2, num):
        if (num % i) == 0:
            isPrime = True
            break
if isPrime:
    print(str(num) + " is not a prime number")
else:
    print(str(num) + " is a prime number")
