# Write an algorithm that simulates the withdrawal of an amount of money from an ATM.
# The algorithm should ask for the amount of the current balance and the amount of the withdrawal.
# If the amount of the withdrawal is greater than the balance, display an error message;
# otherwise, display the new balance.
import random

############################################- version 1 -###############################################################

#current = float(input("Uhm... this is embarrassing but I forgot how much you had in your bank account... I'm sure you"
#                      "wouldn't lie to me so could you just tell me how much you had? Amount :"))
#withdrawal = float(input("How much you wanna take out? Amount :"))
#if current - withdrawal < 0:
##    print("That too much, you don't have enough money!")
#else:
#    current -= withdrawal
#    print("You now have " + str(current) + "$ in your account.")

############################################- version 2 -###############################################################
class bank:
    name = ""
    money =0

    def Deposit(self, depositAmount):
        self.money += depositAmount
        self.Balance()

    def Withdrawal(self, withdrawAmount):
        self.money -= withdrawAmount
        self.Balance()

    def Create(self):
        self.Delete()
        self.name = str(input("Hello user, please enter your name: "))
        self.money = random.randrange(1, 20) * random.randrange(50,  150)


    def Delete(self):
        name=""
        money = 0

    def Balance(self):
        print("The current balance in " + self.name + " is: " + str(self.money) + "$")

currentBank = bank()
inSession = True
print("Initializing...\nNo account found\nCreating new account...")
currentBank.Create()

while inSession:
    print("1 - Check balance\n2 - Deposit amount \n3 - Withdraw amount\n4 - Create new account\n5 - Delete account\n6 - Exit")
    userChoice = int(input("Good Day, please make your select: "))
    if((userChoice<1) or (userChoice>6)):
        print("Invalid choice")
    else:
        match userChoice:
            case 1:
                currentBank.Balance()

            case 2:
                currentBank.Deposit(float(input("Please enter the amount you wish to deposit: ")))

            case 3:
                currentBank.Withdrawal(float(input("Please enter the amount you wish to withdraw: ")))

            case 4:
                validator = int(input("You are about to leave your current bank account and create another one, are you sure?\n1 - Yes\n2 - No\nChoice: "))
                if validator != 1:
                    print("Taking you back to the main menu")
                else:
                    currentBank.Create()

            case 5:
                validator = int(input("You are about to PERMANENTLY delete your account, are you sure?\n1 - Yes\n2 - No\nChoice: "))
                if validator != 1:
                    print("Taking you back to the main menu")
                else:
                    currentBank.Delete()
                    print("Account deleted.\nShutting off the program\nBye bye")
                    inSession = False

            case 6:
                print("Thank you for using my epic ATM machine, bye bye!!")
                inSession = False
