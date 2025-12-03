class Bank:
    def __init__(self,name):
        self.name = name
        self.__balance = 0
        print(f"Welcome to your SBI (Simple Bank of India) {self.name}\n")
    def deposit(self,amt):
        self.__balance += amt
        print(f"{amt} is credited to your bank account\nYour current balance is {self.__balance}")
    def withdraw(self,amt):
        if amt > self.__balance:
            print("Insufficient balance try again\n Cancelling transaction")
        else:
            self.__balance-=amt
            print(f"{amt} is debited from your bank account\n Your cuurent balance is {self.__balance}")

b =Bank("AJ")
b.deposit(500)
b.withdraw(200)
b.withdraw(1000)