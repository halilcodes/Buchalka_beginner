import datetime
import pytz


class Account:

    def __init__(self, name: str, balance: float):
        self.name = name
        self.balance = balance
        self.transaction_list = [(pytz.utc.localize(datetime.datetime.utcnow()), balance)]
        print(f"Account created for {self.name}")

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if self.balance >= amount > 0:
            self.balance -= amount
            self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), -amount))
        else:
            print(f"unable to withdraw. account:{self.balance} - request:{amount}")

    def show_balance(self):
        print(f"Balance is {self.balance}")
        return self.balance

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print(f"{amount:6} {tran_type} on {date} (local time was {date.astimezone()})")


if __name__ == "__main__":
    halil = Account("Halil", 5000.5)
    halil.show_balance()

    halil.deposit(1380)
    halil.deposit(100)
    halil.deposit(13330)

    halil.withdraw(5000)
    halil.withdraw(200)
    halil.withdraw(1590)
    halil.show_transactions()

