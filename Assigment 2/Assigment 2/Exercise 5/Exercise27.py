# An automobile insurance company wants to computerize the calculation of renewals for the premiums of its clients.
# The increase of a client’s premium is a function of the number of accidents, according to the table below:
#
# Number of accidents	Increase
#       0   	            2%
#       1 or 2	            5%
#       3	                10%
#       4 and more	        30%
#
# 	You are asked to create a program that calculates the new value of a premium,
# 	according to the old premium and the number of accidents.

oldPremium = float(input("Please enter your old premium: "))
newPremium = oldPremium

accident = int(input("Please enter the number of accident you had last year: "))
if accident == 0:
    newPremium = newPremium + (newPremium * 0.02)
else:
    if accident <3 :
        newPremium = newPremium + (newPremium * 0.05)
    else:
        if accident == 3 :
            newPremium = newPremium + (newPremium * 0.1)
        else:
            newPremium = newPremium + (newPremium * 0.3)

print("Your old premium was: " + str(oldPremium) + "$\nYour new premium is: " + str(newPremium) +
      "$\nAn increase of: " + str(newPremium - oldPremium) + "$")