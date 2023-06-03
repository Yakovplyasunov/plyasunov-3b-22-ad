class Bank:
    def __init__(self):
        self.clients = {}
        self.transactions = {}
        self.transactions_amount = 0

    def create_client(self, name):
        if name not in self.clients:
            self.clients[name] = {}

    def create_account(self, name, account, balance):
        if name in self.clients and account not in self.clients[name]:
            self.clients[name][account] = balance

    def transfer(self, sender, sender_account, receiver, receiver_account, sum):
        if self.clients[sender][sender_account] >= sum:
            self.clients[sender][sender_account] -= sum
            self.clients[receiver][receiver_account] += sum
            print(f"Перевод успешно выполнен. {sender} перевел {sum} на счет {receiver}.")
            self.transactions_amount += 1
            self.transactions[self.transactions_amount] = {}
            self.transactions[self.transactions_amount]['sender'] = sender
            self.transactions[self.transactions_amount]['receiver'] = receiver
            self.transactions[self.transactions_amount]['sender_account'] = sender_account
            self.transactions[self.transactions_amount]['receiver_account'] = receiver_account
            self.transactions[self.transactions_amount]['sum'] = sum
        else:
            print("Недостаточно средств")
