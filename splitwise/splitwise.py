from user import User
from expense import Expense
from logbook import LogBook
from transaction import Transaction

class Splitwise:
    def __init__(self):
        self.users = {}
        self.logbook = LogBook()

    def add_user(self, name: str):
        if name in self.users:
            raise ValueError(f"User '{name}' already exists.")
        if name == "":
            raise ValueError("Username cannot be empty.")
        user = User(id=len(self.users) + 1, name=name)
        self.users[name] = user

    def add_expense(self, payer: str, amount: float, participants: list[str], description: str = ""):
        if payer not in self.users:
            raise ValueError(f"User '{payer}' does not exist.")
        if any(participant not in self.users for participant in participants):
            raise ValueError("One or more participants do not exist.")
        if len(participants) == 0:
            raise ValueError("At least one participant is required.")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        split_participants = [self.users[participant] for participant in participants]
        expense = Expense(payer=self.users[payer], amount=amount, participants=split_participants, description=description)
        transactions = expense.get_transactions()
        for transaction in transactions:
            self.logbook.add_log(transaction)

    def show_transactions(self):
        print("==== Transactions ====")
        for log in self.logbook.get_logs():
            print(log)
        print("====================\n")

    def show_balances(self):
        print("==== User Balances ====")
        for user in self.users.values():
            print(user)
        print("======================\n")

    def show_user_balance(self, name: str):
        print(f"==== Balance for {name} ====")
        if name not in self.users:
            raise ValueError(f"User '{name}' does not exist.")
        user = self.users[name]
        print(f"{user.name} balance: {user.balance}")
        print("==========================\n")

    # Core Splitwise algorithm: produce a minimal set of settlement transactions
    def show_simplified_transactions(self):
        print("==== Simplified Transactions ====")

        balances = {user.name: user.balance for user in self.users.values()}
        debtors = [(name, -amount) for name, amount in balances.items() if amount < 0]
        creditors = [(name, amount) for name, amount in balances.items() if amount > 0]

        if not debtors and not creditors:
            print("All settled!")
            return
        
        # Sort so largest amounts are settled first (greedy)
        debtors.sort(key=lambda x: x[1], reverse=True)
        creditors.sort(key=lambda x: x[1], reverse=True)

        i = j = 0
        while i < len(debtors) and j < len(creditors):
            debtor_name, debtor_amount = debtors[i]
            creditor_name, creditor_amount = creditors[j]
            settle_amount = min(debtor_amount, creditor_amount)
          
            # make the settlement transaction
            print(f"{debtor_name} owes {creditor_name}: {settle_amount}")
            debtor_amount -= settle_amount
            creditor_amount -= settle_amount

            # update the lists with the new amounts
            if debtor_amount == 0:
                i += 1
            else:
                debtors[i] = (debtor_name, debtor_amount)

            if creditor_amount == 0:
                j += 1
            else:
                creditors[j] = (creditor_name, creditor_amount)  
        print("==============================\n")

    def settle(self, from_user: str, to_user: str, amount: float):
        if from_user not in self.users:
            raise ValueError(f"User '{from_user}' does not exist.")
        if to_user not in self.users:
            raise ValueError(f"User '{to_user}' does not exist.")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        transaction = Transaction(from_user=self.users[to_user], to_user=self.users[from_user], amount=amount, description="Settlement")
        self.logbook.add_log(transaction)