# An electricity bill is calculated by obtaining the number of days for which electricity is supplied and the number of
# kilowatt hours (kWh) consumed. The client is billed at a rate of $0.50 per day and $0.30 per kWh.
# For a client that has consumed more than 200 kWh, their rate is reduced from $0.30 to $0.20 for additional kWh.
# We want to obtain the total amount for the bill.

days = int(input("Please enter how many days you were given electricity: "))
kwh = int(input("Please enter how many kwh you consumed: "))
price = 0.0
if kwh > 200:
    totalPrice = (kwh * 0.3) + (days * 0.5)
    kwh -= 200
    price = (days * 0.5) + (kwh * 0.20) + (200 * 0.30)
    print("kwh : " + str(kwh + 200) +
          "\ndays : " + str(days) +
          "\nTotal before discount: " + str("{:.2f}".format(totalPrice)) +
          "\nBulk discount : " + str("{:.2f}".format((kwh * 0.20) - (kwh * 0.30))) + "$" +
          "\nTotal amount : " + str("{:.2f}".format(price)) + "$")
else:
    price = (days * 0.5) + (kwh * 0.30)
    print("kwh : " + str(kwh) + "\ndays : " + str(days) + "\nTotal amount : " + str("{:.2f}".format(price)) + "$")
