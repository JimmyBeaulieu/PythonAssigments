# Write a program that displays all the prime numbers from 1 to 50,000.

# while loop

Number = 0
a = 1
i = 2
while a < 50001:
    count = 0
    Number += 1
    for i in range(2, (Number//2 + 1)):
        if Number % i == 0:
            count = count + 1
            break
    a += 1
    if count == 0 and Number != 1:
        print(str(Number) + " is a prime number!")
    else:
        print(str(Number) + " is NOT a prime number!")
