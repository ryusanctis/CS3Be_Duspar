class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
    
    def set_account_number(self, account_number):
        self.__account_number = account_number
    
    def get_account_number(self):
        return self.__account_number

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        elif balance < 0:
            print("\nBalance cannot be a negative number, bank balance will be reset to initial balance before change.")
    
    def get_balance(self):
        return self.__balance

Ba1 = BankAccount(1341, 51)

print(f"Account number: {Ba1.get_account_number()}")
print(f"Bank Account Balance: {Ba1.get_balance()}")

Ba1.set_account_number(14212)
Ba1.set_balance(-4214215)

balance = Ba1.get_balance()

print(f"Bank Account Balance set to: {balance}")
print(f"\nAccount number: {Ba1.get_account_number()}")
print(f"Bank Account Balance: {Ba1.get_balance()}")
