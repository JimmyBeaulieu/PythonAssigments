# Write a program that calculates the average of 1000 grades. The program asks the user for each of the grades.

# for loop

grade = 0
totalGrade = 0
for i in range(0, 1000):
    grade = float(input("Please enter grade #" + str(i+1)))
    totalGrade += grade
result = totalGrade / 1000
print("The total average is: " + str(result))
