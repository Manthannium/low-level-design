from user import User
from transaction import Transaction

class Expense:
    def __init__(self, payer: User, participants: list[User], amount: float, description: str = ""):
        self.payer = payer
        self.amount = amount
        self.participants = participants
        self.description = description
        self.transactions = self.create_transactions()

    def create_transactions(self) -> list[Transaction]:
        transactions = []
        split_amount = self.amount / len(self.participants)
        for participant in self.participants:
            if participant.user_id != self.payer.user_id:
                transactions.append(Transaction(from_user=participant, to_user=self.payer, amount=split_amount, description=self.description))
        return transactions
    
    def get_transactions(self):
        return self.transactions