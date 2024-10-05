# class BankAccount:
#     def __init__(self, initial_balance=0.0):
#         self.__account_balance = initial_balance

#     def deposit(self, amount):
#         if amount <= 0:
#             print("Deposit amount must be positive.")
#             return
#         self.__account_balance += amount

#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Withdrawal amount must be positive.")
#             return False
#         if amount > self.__account_balance:
#             return False
#         self.__account_balance -= amount
#         return True

#     def display_balance(self):
#         print(f"Current Balance: ${self.__account_balance:.2f}")
        
        
class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance  # Private attribute to encapsulate balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        if amount > 0 and self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.2f}")

