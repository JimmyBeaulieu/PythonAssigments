# Monique want to have a little program that allows her to evaluate the total amount of her expenses for a month,
# as well as the amount of money she can allocate for her leisure activities and non-essential spending.
# The program should read her projections for expenses in the following categories:
# Weekly expenses (one time per week; assuming that 1 month = 4 weeks)
#•	Food expenses and household expenses
#•	Common expenses
# Monthly expenses (one time per month)
#•	Public transit pass
#•	Rent
#•	Total of monthly bills
# The program should also read the amount of her paycheques. Monique receives two paycheques per month.
#T he program should then display her total expenses, her total income, and the difference.

weekly = float(input("Food: "))
weekly += float(input("Household expense: "))
weekly += float(input("Common expenses: "))
weekly *= 4
monthly = float(input("Public transit pass: "))
monthly += float(input("Rent: "))
monthly += float(input("Monthly bills: "))
pay = float(input("Paycheck: "))
pay *= 2
print("Your total expenses this month are: " + str(weekly + monthly))
print("Your total revenue this month are: " + str(pay))
print("Monique, you made " + str(pay - (weekly + monthly)) + "$ this month")
