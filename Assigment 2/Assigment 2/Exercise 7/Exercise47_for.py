# Write a program that reads the grades for the exams and assignments in a course including 2 exams and 2 assignments.
# The program should be able to adapt to the conditions of the course. More precisely:
# x	The program should read the number of students in the course.
# x	For each of the four grades, ask the user what the weight of the grade is.
#   In other words, how much is the grade worth as a percentage of the final grade for the course?
# >	The program should validate that the total of the four weights given is indeed equal to 100.
# >	Then, for each student, the program should read the student’s four grades (each out of 100).
#   Verify that the values entered are between 0 and 100. Then calculate the final course grade for each student.
# >	The program should display whether the student passes or fails the course.
#   A student passes if they achieve 60 or greater.
# >	Finally, the program should display the average of all the students’ final course grades.

# for loop

class Student:
    def __init__(self):
        self.exam1Result = 0
        self.exam2Result = 0
        self.assignment1Result = 0
        self.assignment2Result = 0

        self.exam1Weight = 0
        self.exam2Weight = 0
        self.assignment1Weight = 0
        self.assignment2Weight = 0

        self.exam1Final = 0
        self.exam2Final = 0
        self.assignment1Final = 0
        self.assignment2Final = 0

    def calculate(self):
        self.exam1Final = self.exam1Result * (self.exam1Weight / 100)
        self.exam2Final = self.exam2Result * (self.exam1Weight / 100)
        self.assignment1Final = self.assignment1Result * (self.assignment1Weight / 100)
        self.assignment2Final = self.assignment2Result * (self.assignment2Weight / 100)
        return self.exam1Final + self.exam2Final + self.assignment1Final + self.assignment2Final


classroom = []
numberOfStudent = 0
checker = False

while numberOfStudent == 0:
    numberOfStudent = int(input("How many students are we talking about: "))
    if numberOfStudent < 1:
        print("Please enter at least one student!")

while not checker:
    i = 0
    for x in range(0, numberOfStudent):

        student = Student()

        student.exam1Weight = int(input("What's the weight of the first exam in percentage ('10%' = '10')? :"))
        student.exam2Weight = int(input("What's the weight of the second exam ('10%' = '10')? :"))
        student.assignment1Weight = int(input("What's the weight of the first assignment ('10%' = '10')? :"))
        student.assignment2Weight = int(input("What's the weight of the second assignment ('10%' = '10')? :"))

        if student.exam1Weight + student.exam2Weight + student.assignment1Weight + student.assignment2Weight == 100:
            student.exam1Result = int(input("Enter result for first exam: "))
            student.exam2Result = int(input("Enter result for second exam: "))
            student.assignment1Result = int(input("Enter result for first assignment: "))
            student.assignment2Result = int(input("Enter result for second assignment: "))

            if student.calculate() < 60:
                print("Student #" + str(i + 1) + " did not pass their semester...")
            if student.calculate() >= 60:
                print("Student #" + str(i + 1) + " passed their semester!!!")

            checker = True
            classroom.append(student)
            print("Number of student entered so far: " + str(len(classroom)))
            i += 1
        else:
            print("Cumulative weight does not equal 100%, please enter them again")

i = 0
total = 0
for x in range(0, len(classroom)):
    total += classroom[i].calculate()
    i += 1
classAverage = total / len(classroom)
print("The average for the whole class is: " + str(classAverage))
