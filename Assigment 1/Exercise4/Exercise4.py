# The Ministère des Finances of Québec is adopting a project aiming to reduce taxes.
# Develop an algorithm that calculates taxes according to the table provided below.
# In addition, a 2% reduction of the tax rate is granted if the person is married.
# Furthermore, a 0.5% reduction is granted for each child.
# Finally, 8% is subtracted from the tax rate for those who have newly arrived in the province.
# Determine the amount of tax to be paid as a function of the information provided by the user.

# Salary	Tax rate
# $0.00 to $18,000.00    	10%
# $18,000.01 to $32,000.00 	20%
# $32,000.01 to $60,000.00 	30%
# $60,000.01 and more	    40%

amount = int(input("Please enter how much money you made this year: "))
reduction = 0
married = input("Are you married?\nY/N:")
if married == "y" or married == "Y":
    reduction += 0.02

children = int(input("How many children do you own: "))
reduction += (children * 0.005)

immigrant = input("Are you newly arrived in the province?\nY/N")
if (immigrant == "Y") or (immigrant == "y"):
    reduction += 0.08
taxRate = 0
if amount < 18001:
    taxRate = 0.1
if amount >18000 and amount < 32001:
    taxRate = 0.2
if amount > 32000 and amount < 60001:
    taxRate = 0.3
if amount > 60001:
    taxRate = 0.4

taxRate -= reduction

print("The total gross revenu was: " + str(amount))
print("The total discount was: " + (str(amount - (amount * taxRate))))
print("The tax rate is: " + str(taxRate * 100) + "%")
print("Total amount owed for your taxes: " + str(amount * taxRate))
