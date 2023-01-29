# 24 –	We want to create a program that displays the letter grade for a student, given their grade in percentage,
# according to the following table:

#  Grade	Letter
#  90% – 100%	A
#  80% – 89% 	B
#  70% – 79%	C
#  60% – 69%	D
#< 60% 	F

grade = float(input("Please enter your grade: "))
letterGrade = ""
if grade > 89:
    letterGrade = "A"
if grade < 90 and grade > 79 :
    letterGrade = "B"
if grade < 80 and grade > 69 :
    letterGrade = "C"
if grade < 70 and grade > 59 :
    letterGrade = "D"
if grade < 60:
    letterGrade = "F"

print("Your grade in letter is: " + letterGrade)