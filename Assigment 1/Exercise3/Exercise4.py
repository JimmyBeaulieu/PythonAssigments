# A print shop charges 5 cents per copy for the first 100 copies. For any subsequent copies, they charge 3 cents each.
# Write an algorithm that determines the price associated with a given number of copies.


page = float(input("How many copy do you need?:"))
if page > 100:
    price = (page-100) * 0.03
    price += 5;
else:
    price = page * 0.05
print("Please pay " + str("{:.2f}".format(price)) + "$")
