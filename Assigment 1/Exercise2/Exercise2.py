# An aircraft pilot wants to know the atmospheric pressure, expressed in atmosphere units (atm),
# as the weather station only provides pressure data in kilopascal units (kPa).
# 1 atm is equivalent to 101.325 kPa. Make a program that performs the conversion.

userInput = float(input("kPa: "))
print(str(userInput) + str(" kpa = ") + str(userInput/101.325) + str(" atm"))
