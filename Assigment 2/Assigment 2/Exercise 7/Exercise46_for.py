# Write a program that displays all the prime numbers from 1 to 50,000.

# for loop

for Number in range(1, 50001):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if Number % i == 0:
            count = count + 1
            break

    if count == 0 and Number != 1:
        print(str(Number) + " is a prime number!")
