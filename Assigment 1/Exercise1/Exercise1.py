# In the old system of calculating sales tax in Québec, the taxes on a product were 7% for the GST, and 7.5% for
# the QST (applied after calculating the GST).
# Make a program that reads the unit price of a product and the quantity purchased, and that displays the amounts for
# the GST, the QST, and the total price after taxes.

price = float(input("Enter your price:"))
GST = 0.07
QST = 0.075
print("Original price: "+str(price))
print("GST: "+str(price * GST))
print("QST: "+str(price * QST))
print("Final price: "+str(price + (price * GST)+(price*QST)))
