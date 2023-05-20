class BankAccount:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Счет пополнен на {amount}. Баланс равен {self.balance}')
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'Со счета снято {amount}. Баланс равен {self.balance}')
        else:
            print(f'Недостаточно средств на счету')
        return self.balance
