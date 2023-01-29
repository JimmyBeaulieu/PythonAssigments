# Create four algorithms, each displaying the corresponding one of the following sequences:
#
# a)		5	10	15	20	25	30	35	40
# b)		3	5	7	9	11	13	15
# c)		80	70	60	50	40	30	20
# d)		1	2	6	24	120	720

# for loop
value = 0
valueString = ""
for x in range(0, 8):
    value += 5
    valueString += str(value) + " "
print("a)   " + valueString)

value = 1
valueString = ""
for x in range(0, 7):
    value += 2
    valueString += str(value) + " "
print("b)   " + valueString)

value = 90
valueString = ""
for x in range(0, 7):
    value -= 10
    valueString += str(value) + " "
print("c)   " + valueString)

value = 1
valueString = ""
i = 1
for x in range(0, 6):
    value = value * i
    i += 1
    valueString += str(value) + " "
print("d)   " + valueString)
