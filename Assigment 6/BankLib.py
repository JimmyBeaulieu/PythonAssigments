class BankAccount:

    def __init__(self, firstName, lastName, accountNumber, money):
        self.firstName = firstName
        self.lastName = lastName
        self.accountNumber = accountNumber
        self.money = money

    def DisplayInformation(self):
        print("Account Number: " + str(self.accountNumber) + "\n" +
              "Name: " + self.firstName + " " + self.lastName + "\n" +
              "Current Balance: " + str(self.money))

    def AddMoney(self, amount):
        self.money += amount

    def WithdrawMoney(self, amount):
        self.money -= amount

    def DisplayMoney(self):
        print("Money : " + self.money)
