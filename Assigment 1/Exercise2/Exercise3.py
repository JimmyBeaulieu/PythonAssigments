# In a computer technology course, the following evaluation weights are used:
# Laboratory work counts for 40% of the grade
# The midterm exam counts for 25%
# The final exam counts for 35%

lab = float(input("Laboraty work results: "))
midterm = float(input("Midterm results: "))
final = float(input("Final results: "))
print("your final grade is: "+str((lab*0.4)+(midterm*0.25)+(final*0.35))+"%")