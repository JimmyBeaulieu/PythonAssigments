# You just won a million dollars! You decide to invest $500,000 in a term deposit for a period of 5 years.
# The annual interest rate is 10%, and the interest is added to the principal sum each year (compound interest).
# How much will your savings be worth in 5 years?
#
# a)	Make the algorithm with specified number (internal data).
# b)	Generalize for any amount, any duration, and any interest rate.

# while loop

# Generalized version
money = float(input("Please enter how much you won: "))
interest = float(input("Please enter the interest rate (format: 10% = '10': "))
time = int(input("Please enter how many years: "))

# internal data version
# money = 500000
# interest = 10
# time = 5
finalMoney = 0

i = 0
while i < time:
    finalMoney = money + ((money * (interest/100)) * time)
    i += 1
print(str(money) + "$ becomes " + str(finalMoney) + "$ after " + str(time) + "years at an interest rate of " +
      str(interest) + "%")

