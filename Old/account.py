import os
import time
from datetime import datetime, timedelta, timezone


class Account:
    transaction_counter = 0
    interest_rate = 0.5
    _transaction_codes = {"Deposit":"D", "Withdraw":"W","Interest":"I","Reject":"X"}
    transactions = []
    float(interest_rate)
    def __init__(self, account_number, first_name, last_name, time_zone,balance):
        self._account_number = account_number
        self._first_name = first_name
        self._last_name = last_name
        self._time_zone = time_zone
        self._balance = balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @first_name.setter
    def first_name(self,value):
        self.first_name = value

    @last_name.setter
    def last_name(self, value):
        self.last_name = value

    @property
    def time_zone(self):
        return self._time_zone

    @property
    def balance(self):
        return self._balance

    @classmethod
    def display_interest(cls):
        return cls.interest_rate

    @classmethod
    def set_interest_rate(cls,value):
        if cls.interest_rate <= 0:
            print("Non existent interest rate cuh.")
        elif cls.interest_rate == str:
            print("You cannot enter an string as an interest rate.")
        cls.interest_rate = value

    def generate_transaction_number(self,transaction_code):
        timestamp_utc = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
        Account.transaction_counter += 1
        confirmation_number = f"{transaction_code}-{self.account_number}-{timestamp_utc}-{Account.transaction_counter}"
        return confirmation_number

    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("Deposit a legitimate amount")

        self._balance += amount
        confirmation_code = self.generate_transaction_number(Account._transaction_codes["Deposit"])
        Account.transactions.append(f"Transaction : {Account.transaction_counter},"
                                 f"Confirmation Number : {confirmation_code},"
                                 f"Amount : {amount},"
                                 f"Account Number : {self.account_number},"
                                 f"Type : Deposit,"
                                 f"Balance After: {self.balance}")
        print(f"{amount} has been deposited to your bank account Mr {self.first_name} and your current balance is {self.balance}")



    def withdraw(self,amount):
        if amount > self._balance or amount <= 0:
            confirmation_code = self.generate_transaction_number(Account._transaction_codes["Reject"])
            Account.transactions.append(f"Transaction : {Account.transaction_counter},"
                                        f"Confirmation Number : {confirmation_code},"
                                        f"Amount : {amount},"
                                        f"Account Number : {self.account_number},"
                                        f"Type : Withdrawal,"
                                        f"Balance After: {self.balance}")
            print("The amount you are trying to withdraw is non existent.")
            quit()

        self._balance -= amount
        confirmation_code = self.generate_transaction_number(Account._transaction_codes["Withdraw"])
        Account.transactions.append(f"Transaction : {Account.transaction_counter},"
                                 f"Confirmation Number : {confirmation_code},"
                                 f"Amount : {amount},"
                                 f"Account Number : {self.account_number},"
                                 f"Type : Withdrawal,"
                                 f"Balance After: {self.balance}")
        print(f"{amount} has been withdrew to your bank account Mr {self.first_name} and your current balance is {self.balance}")

    def pay_interest(self):
        interest = (self.balance * Account.interest_rate * 1)/100
        self._balance += interest
        confirmation_code = self.generate_transaction_number(Account._transaction_codes["Interest"])
        Account.transactions.append(f"Transaction : {Account.transaction_counter},"
                                    f"Confirmation Number : {confirmation_code},"
                                    f"Account Number : {self.account_number},"
                                    f"Type : Withdrawal,"
                                    f"Balance After: {self.balance}")
        print(f"Your monthly interest is {interest}")

Banker = Account("123457", "Vihaan", "Khullar", "IST", 1000)
Banker.deposit(1000)
Banker.withdraw(1000)
Banker.set_interest_rate(8)
Banker.pay_interest()
print(Banker.balance)
print(Banker.transactions)