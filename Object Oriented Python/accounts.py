import datetime
import pytz


class Account:
    """ Simple account class with balance """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print("Account created for {} in the amount of {}".format(self._name, str(self._balance)))

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print("Adding " + str(amount))
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdrawl(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print("Withdrawing " + str(amount))
        else:
            print("Cancelling withdrawl...You will be overdrawn if you withdraw {}.".format(amount))
        self.show_balance()
        self._transaction_list.append((Account._current_time(), -amount))

    def show_balance(self):
        print("Balance is {}".format(self._balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    checking = Account("Paul", 1000)

    checking.deposit(600)
    checking.withdrawl(2010)
    checking.withdrawl(1400)
    checking.show_transactions()

    steve = Account("Steve", 800)
    steve.deposit(100)
    steve.withdrawl(200)
    steve.show_transactions()
