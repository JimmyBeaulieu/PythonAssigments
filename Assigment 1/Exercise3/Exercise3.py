# A computer store sells diskettes at a price of $1 each for small orders.
# The store sells them at a price of 70 cents each for orders of 25+ units.
# Furthermore, if you are a member of Club Z, the store will give you an extra discount of 2%.
# Write an algorithm that determines the total price for a purchase.

amount = float(input("Amount of diskette you are buying : "))
if amount > 25:
    print("Big order discount = -" + str(amount - (amount * 0.7)))
    amount *= 0.7
membership = str(input("Are you a member of Club Z? (y/n)"))
if membership == "y":
    amount = amount - (amount * 0.02)
    print("The total amount is: " + str(amount))
else:
    print("The total amount is: " + str(amount))
