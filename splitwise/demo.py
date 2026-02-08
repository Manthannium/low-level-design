from splitwise import Splitwise

if __name__ == "__main__":
    s = Splitwise()

    s.add_user("Alice")
    s.add_user("Bob")
    s.add_user("Charlie")

    s.add_expense(payer="Alice", amount=120, participants=["Alice", "Bob", "Charlie"], description="Dinner")
    s.add_expense(payer="Bob", amount=60, participants=["Alice", "Bob"], description="Drinks")
    s.add_expense(payer="Charlie", amount=90, participants=["Bob", "Charlie"], description="Groceries")

    s.show_transactions()
    s.show_balances()
    s.show_user_balance("Alice")
    s.show_simplified_transactions()

    s.settle(from_user="Bob", to_user="Alice", amount=50)
    s.show_balances()
    s.show_transactions()
    s.show_simplified_transactions()