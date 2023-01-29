# A palindrome is a number, a word, or a sentence that remains identical whether read from left to right or
# from right to left. For example, each of the following five-digit numbers is a palindrome:
# 12321, 55555, 45554, 11611.
# Write a program capable of reading a positive integer (greater than 0) with five digits,
# and of determining whether this integer is a palindrome.
# (Hint: use the modulus and division operators to separate the different digits composing the numbers.)

num = input('Enter any number : ')
try:
    val = int(num)
    if num == str(num)[::-1]:
        print('The given number is PALINDROME')
    else:
        print('The given number is NOT a palindrome')
except ValueError:
    print("That's not a valid number, Try Again !")
