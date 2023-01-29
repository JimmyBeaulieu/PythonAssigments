# Write an algorithm that displays a table for converting Celsius units into Fahrenheit units.
# The table should display all the values from –40 to 40 degrees Celsius, at increments of 5 degrees.
# The conversion formula is:
# F=9/5  ×C+32
f = -40
c = -40
while c != 41:
    a = 9 / 5 * f + 32
    print(str(c) + "°C is " + str(a) + "°F")
    f = f + 1
    c = c + 1
