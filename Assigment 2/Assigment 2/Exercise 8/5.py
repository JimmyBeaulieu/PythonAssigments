# Write a program that reads the radius of a circle, and that displays
# the diameter, the circumference, and the area of the circle.
# Use the constant value 3.14159 for π.

PI = 3.14159

radius = int(input("Please enter the radius: "))

print("The diameter is: " + str(radius * 2))
print("The circumference is: " + str((2 * PI) * radius))
print("The area is: " + str(PI * (pow(radius, 2))))
