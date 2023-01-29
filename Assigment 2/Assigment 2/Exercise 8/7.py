# A large chemical products company compensates its commercial representatives by commission.
# The representatives receive $200 per week plus 9% of their gross sales per week.
# For example,
# a representative who sells $5000 of chemical products in one week receives a salary of $200 plus 9% of $5000,
# for a total of $650.
# Develop a program that asks for the gross weekly sales of each representative
# and that calculates and displays their salary. Process the information of one representative at a time.
#
# Example of the program’s execution:
# Enter the representative’s sales in dollars (-1 to terminate):
# 5000.00
# The representative’s salary is $650.00.

grossSales = float(input("Enter the representative's sales in dollars (-1 to terminate): "))
if grossSales == -1:
    quit()
salary = (grossSales * 0.09) + 200
print("The representative's salary is " + str(salary))
