from transaction import Transaction

class LogBook:
    def __init__(self):
        self.logs: list[str] = []

    def add_log(self, transaction: Transaction):
        self.logs.append(str(transaction))

    def print_logs(self):
        for log in self.logs:
            print(log)

    def get_logs(self):
        return self.logs