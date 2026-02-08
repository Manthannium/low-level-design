from user import User

class Transaction:
    def __init__(self, from_user: User, to_user: User,  amount: float, description: str = ""):
        self.from_user = from_user
        self.to_user = to_user
        self.amount = amount
        self.description = description
        self.execute_transaction()

    def execute_transaction(self):
        self.from_user.update_balance(-self.amount)
        self.to_user.update_balance(self.amount)

    def __str__(self):
        return f"{self.from_user.name} owes {self.to_user.name}: {self.amount}"