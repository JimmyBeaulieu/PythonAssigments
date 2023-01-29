# Create a prototype of a program that simulates a bank. More precisely, the program should be able to store the family
# name and given name of a client, their unique account number (a number between 10000 and 10099), and the balance of
# their account.
import sys

# The program should display a menu with the following options:
# 1.	Add a bank account.
# 2.	Remove a bank account.
# 3.	Display the information of a particular client’s account. (by account number)
# 4.	Apply a deposit to a particular account. (by account number)
# 5.	Apply a withdrawal from a particular account. (by account number)
# 6.	Sort and display the list of clients according to their balance, family name and given name,
# in ascending or descending order.
# 7.	Display the average balance value of the accounts.
# 8.	Display the total balance value of the accounts.
# 9.	Exit the application.

# You must implement each of these functionalities.
#
# Remarks:
# •	The maximum number of accounts for this application is 100 accounts.
# •	All input must be validated. (type, length , no duplicate)
# •	Each task out of the various functionalities should be delegated to an appropriate function.

import BankLib

bankDatabase = []
accountNumber = 10000

while True:
    while True:
        print("Bank")
        print("1.	Add a bank account.\n"
              "2.	Remove a bank account.\n"
              "3.	Display the information of a particular client’s account. (by account number)\n"
              "4.	Apply a deposit to a particular account. (by account number)\n"
              "5.	Apply a withdrawal from a particular account. (by account number)\n"
              "6.	Sort and display the list of clients\n"          
              "7.	Display the average balance value of the accounts.\n"
              "8.	Display the total balance value of the accounts.\n"
              "9.	Exit the application.")
        try:
            choice = int(input("Please give me your select:"))
            break
        except:
            print("\n#-#-#-#-#-#-#-#-#-#")
            print("\nERROR: Please only enter a number corresponding to the menu\n")
            print("#-#-#-#-#-#-#-#-#-#\n")

    if choice == 1:
        firstName = input("Please enter your first name: ")
        lastName = input("Please enter your last name: ")
        while True:
            try:
                money = int(input("Please enter your initial amount of money: "))
                break
            except:
                print("\n#-#-#-#-#-#-#-#-#-#")
                print("\nERROR: Please enter an integer representing an amount\n")
                print("#-#-#-#-#-#-#-#-#-#\n")

        account = BankLib.BankAccount(firstName, lastName, accountNumber, money)
        account.DisplayInformation()
        accountNumber += 1
        bankDatabase.append(account)
        print("Account added successfully!")

    if choice == 2:
        while True:
            try:
                number = int(input("Please enter the number of the account you want to delete:"))
                break
            except:
                print("\n#-#-#-#-#-#-#-#-#-#")
                print("\nERROR: Please enter an integer corresponding to an account number (ex: 10000)\n")
                print("#-#-#-#-#-#-#-#-#-#\n")

        for acc in bankDatabase:
            if acc.accountNumber == number:
                choice = input("Found one account, are you sure you want to permanently delete the account?\ny - yes\nanything else - no:")
                if choice == "y" or choice == "Y":
                    bankDatabase.remove(acc)
                    print("Account successfully removed, returning to main menu...\n")
                else:
                    print("returning to main menu...\n")

    if choice == 3:
        flag = False
        while True:
            try:
                number = int(input("Please enter the number of the account you want to display information:"))
                break
            except:
                print("\n#-#-#-#-#-#-#-#-#-#")
                print("\nERROR: Please enter an integer corresponding to an account number (ex: 10000)\n")
                print("#-#-#-#-#-#-#-#-#-#\n")

        for acc in bankDatabase:
            if acc.accountNumber == number:
                acc.DisplayInformation()
                flag = True
            if not flag:
                print("No account found with the provided account number, returning to main menu...")
    if choice == 4:
        while True:
            try:
                number = int(input("Please enter the number of the account you want to display information:"))
                break
            except:
                print("\n#-#-#-#-#-#-#-#-#-#")
                print("\nERROR: Please enter an integer corresponding to an account number (ex: 10000)\n")
                print("#-#-#-#-#-#-#-#-#-#\n")

        for acc in bankDatabase:
            if acc.accountNumber == number:
                while True:
                    try:
                        moneyToAdd = int(input("Account found, please enter the amount to add: "))
                        break
                    except:
                        print("\n#-#-#-#-#-#-#-#-#-#")
                        print("\nERROR: Please enter an integer representing an amount\n")
                        print("#-#-#-#-#-#-#-#-#-#\n")

                acc.AddMoney(moneyToAdd)
    if choice == 5:
        while True:
            try:
                number = int(input("Please enter the number of the account you want to display information:"))
                break
            except:
                print("\n#-#-#-#-#-#-#-#-#-#")
                print("\nERROR: Please enter an integer corresponding to an account number (ex: 10000)\n")
                print("#-#-#-#-#-#-#-#-#-#\n")

        for acc in bankDatabase:
            if acc.accountNumber == number:
                while True:
                    try:
                        moneyToRemove = int(input("Account found, please enter the amount to widthdraw or"
                                                  " enter 0 to return to the main menu: "))
                        break
                    except:
                        print("\n#-#-#-#-#-#-#-#-#-#")
                        print("\nERROR: Please enter an integer representing an amount\n")
                        print("#-#-#-#-#-#-#-#-#-#\n")

                if moneyToRemove > acc.money:
                    print("Error, the amount to withdraw cannot be higher than the current account's balance!")
                if moneyToRemove == 0:
                    break
                else:
                    acc.WithdrawMoney(moneyToRemove)
                    print("Amount successfully withdrew!")

    if choice == 6:
        # 6.	Sort and display the list of clients according to their balance, family name and given name,
        # in ascending or descending order.
        while True:
            try:
                choice = int(input("1. Display all account ordered by balance\n"
                                   "2. Display all account ordered by family name\n"
                                   "3. Display all account by first name\n"
                                   "4. Return to main menu"))
                break
            except:
                print("\n#-#-#-#-#-#-#-#-#-#")
                print("\nERROR: Please enter an integer representing an option on the menu\n")
                print("#-#-#-#-#-#-#-#-#-#\n")

        if choice == 1:
            newArray = sorted(bankDatabase, key=lambda BankAccount: BankAccount.money)

            while True:
                try:
                    order = int(input("1 - Ascending\n2 - Descending:"))
                    break
                except:
                    print("\n#-#-#-#-#-#-#-#-#-#")
                    print("\nERROR: Please enter an integer representing an option ont the menu\n")
                    print("#-#-#-#-#-#-#-#-#-#\n")

            if order == 1:
                for acc in newArray:
                    acc.DisplayInformation()
            if order == 2:
                newArray.sort(key=lambda BankAccount: BankAccount.money, reverse=True)
                for acc in newArray:
                    acc.DisplayInformation()

        if choice == 2:
            newArray = sorted(bankDatabase, key=lambda BankAccount: BankAccount.lastName)

            while True:
                try:
                    order = int(input("1 - Ascending\n2 - Descending:"))
                    break
                except:
                    print("\n#-#-#-#-#-#-#-#-#-#")
                    print("\nERROR: Please enter an integer representing an option ont the menu\n")
                    print("#-#-#-#-#-#-#-#-#-#\n")

            if order == 1:
                for acc in newArray:
                    acc.DisplayInformation()
            if order == 2:
                newArray.sort(key=lambda BankAccount: BankAccount.lastName, reverse=True)
                for acc in newArray:
                    acc.DisplayInformation()
        if choice == 3:
            newArray = sorted(bankDatabase, key=lambda BankAccount: BankAccount.firstName)

            while True:
                try:
                    order = int(input("1 - Ascending\n2 - Descending:"))
                    break
                except:
                    print("\n#-#-#-#-#-#-#-#-#-#")
                    print("\nERROR: Please enter an integer representing an option ont the menu\n")
                    print("#-#-#-#-#-#-#-#-#-#\n")

            if order == 1:
                for acc in newArray:
                    acc.DisplayInformation()
            if order == 2:
                newArray.sort(key=lambda BankAccount: BankAccount.firstName, reverse=True)
                for acc in newArray:
                    acc.DisplayInformation()
        if choice == 4:
            break

    if choice == 7:
        sumamount = 0
        for acc in bankDatabase:
            sumamount += acc.money
        print("The average balance value of all the accounts is: " + str(sumamount / len(bankDatabase)))

    if choice == 8:
        sumamount = 0
        for acc in bankDatabase:
            sumamount += acc.money
        print("The total balance value of all the accounts is: " + str(sumamount))
    if choice == 9:
        sys.exit(0)
