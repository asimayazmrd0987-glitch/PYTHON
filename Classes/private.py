class BankAccount:
    def __init__(self, balance):
        self._balance = balance     # convention: "protected", don't touch outside
        self.__pin = 1234           # name-mangled: "private"-ish

    def deposit(self, amount):
        self._balance += amount

# bank = BankAccount(12)
# bank.deposit()

b = BankAccount(100)
print(b._BankAccount__pin)  # 1234 — "private" is still accessible if you know the mangled name