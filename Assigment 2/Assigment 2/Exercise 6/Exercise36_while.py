# Create four algorithms, each displaying the corresponding one of the following sequences:
#
# a)		5	10	15	20	25	30	35	40
# b)		3	5	7	9	11	13	15
# c)		80	70	60	50	40	30	20
# d)		1	2	6	24	120	720

# while loop
value = 0
valueString = ""
index = 0
while index < 8:
    value += 5
    valueString += str(value) + " "
    index += 1
print("a)   " + valueString)

index = 0
value = 1
valueString = ""
while index < 7:
    value += 2
    valueString += str(value) + " "
    index += 1
print("b)   " + valueString)

index = 0
value = 90
valueString = ""
while index < 7:
    value -= 10
    valueString += str(value) + " "
    index += 1
print("c)   " + valueString)

index = 0
value = 1
valueString = ""
i = 1
while index < 6:
    value = value * i
    i += 1
    valueString += str(value) + " "
    index += 1
print("d)   " + valueString)
