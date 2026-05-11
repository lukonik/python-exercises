class BankAccount:
    def __init__(self, balance: int):
        self.__balance = balance

    def deposit(self, amount: int):
        self.__balance += amount

    def withdraw(self, amount: int):
        if self.__balance < amount:
            print("Insufficient amount current balance is " + str(self.__balance))
            return
        self.__balance -= amount


account = BankAccount(100)
account.deposit(50)
account.withdraw(200)  # This should trigger a warning

