class User:
    def __init__(self, id: int, name: str, balance: float = 0.0):
        self.user_id = id
        self.name = name
        self.balance = balance
    
    def update_balance(self, amount: float):
        self.balance += amount

    def __str__(self):        
        return f"User (id={self.user_id}, name={self.name}, balance={self.balance})"