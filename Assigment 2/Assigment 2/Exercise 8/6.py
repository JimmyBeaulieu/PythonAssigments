# Drivers are concerned with the mileage of their automobiles.
# A driver decides to record the number of kilometers traveled and the number of litres of gasoline used,
# each time they refill their gas tank.
# Develop a program with the goal of being able to enter the number of kilometers
# traveled and the number of litres used upon each gas refill. The program should calculate and display
# the rate of gas consumption (in litres per 100 kilometers) between each gas refill.
# After having processed all the information entered, the program should calculate and
# display the total rate of gas consumption (in litres per 100 kilometers) for all the gas refills.
#
# Example of the program’s execution:
# Enter the number of litres used (-1 to terminate):
# 48.5
# Enter the number of kilometers traveled:
# 459
# The rate of gas consumption in litres per 100 kilometers for this gas refill is 10.566448.

while True:
    liter = float(input("Enter the number of litres used (-1 to terminate): "))
    if liter == -1:
        quit()
    kilometer = float(input("Enter the number of kilometers traveled: "))
    print("The rate of gas consumption in litres per 100 kilometers for this gas refill is " + str((liter / kilometer) * 100))
