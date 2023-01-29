# Write a program that calculates the average of 1000 grades. The program asks the user for each of the grades.

# while loop

grade = 0
totalGrade = 0
i = 0
while i < 1001:
    # grade = float(input("Please enter grade #" + str(i+1)))
    grade = float(input("Please enter grade #" + str(i+1)))
    totalGrade += grade
    i += 1
result = totalGrade / 1000
print("The total average is: " + str(result))
