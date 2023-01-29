# Write an algorithm that reads three numbers and determines whether these numbers,
# considered as the lengths of the three sides of a triangle, would correspond to:

#	An equilateral triangle (three equal sides)
#	An isosceles triangle (two equal sides)
#	A scalene triangle (three different sides)

sidea = float(input("Enter the first side:"))
sideb = float(input("Enter the second side:"))
sidec = float(input("Enter the third side:"))

if(sidea == sideb and sidec == sidea):
    print("This is an equilateral triangle.")
else:
    if(sidea == sideb or sideb == sidec or sidea == sidec):
        print("This is an isosceles triangle.")
    else:
        print("This is a scalene triangle.")
