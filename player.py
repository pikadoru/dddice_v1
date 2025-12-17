class Player:
    
    def __init__(self, name:str, balance=100):
        self.name = name
        self.balance = balance
        self.transactions = []

    def update_balance(self, amount, reason:str):
        self.balance += amount
        self.transactions.append((amount, reason))
    
    def print_transactions(self):
        for amount, reason in self.transactions:
            print(f"{reason}: {'+' if amount >= 0 else ''}{amount} mil")

    def get_balance(self):
        return self.balance

    def get_name(self):
        return self.name