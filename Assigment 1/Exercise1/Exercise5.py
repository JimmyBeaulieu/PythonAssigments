# A dealership selling new vehicles asks you to construct a program that calculates the compensation paid to their
# salespeople. The base salary for all the salespeople is $400.
# For each vehicle sold, the salesperson receives a commission of $200.
# Also, the salesperson receives a bonus of 5% of the total amount of all their sales.
# Make the program for a salesperson.

userInput = int(input("Labourer, enter the number of product sold:"))
commission = userInput * 200
commission = commission + (commission * 0.05)
commission += 400
print("Your commission is:"+str(commission))
