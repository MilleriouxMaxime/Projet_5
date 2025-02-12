class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} a été déposé sur le compte.")
        else:
            print("Le montant du dépôt doit être positif.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"{amount} a été retiré du compte.")
            else:
                print("Fonds insuffisants pour ce retrait.")
        else:
            print("Le montant du retrait doit être positif.")

    def display_balance(self):
        print(f"Titulaire du compte : {self.account_holder}")
        print(f"Solde du compte : {self.balance:.2f} EUR")

# Example usage:
account = BankAccount("Alice", 100.0)
account.display_balance()
account.deposit(50.0)
account.display_balance()
account.withdraw(30.0)
account.display_balance()
account.withdraw(150.0)
account.display_balance()