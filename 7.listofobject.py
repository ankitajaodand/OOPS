import random
from typing import List


class Bank:
    def __init__(self) -> None:
        self.account_number = random.randint(100000, 999999)
        self.holder = input("Enter your name = ").title()
        self.balance = 0.0
        self.account_type = input("Enter account type = ").title()

    def display(self):
        print(f"\nAccount number = {self.account_number}")
        print(f"Account holder = {self.holder}")
        print(f"Account balance = {self.balance}")
        print(f"Account Type = {self.account_type}\n")

    def withdraw(self):
        amt = float(input("Enter amount to withdraw = "))
        if amt < 0:
            print("Invalid amount")
            return
        if self.balance >= amt:
            self.balance -= amt
            print(f"Updated balance = {self.balance}")
        else:
            print("Insuffciient Balance")

    def deposit(self):
        amt = float(input("Enter amount to deposit = "))
        if amt < 0:
            print("Invalid amount")
            return
        self.balance += amt

    def getBalance(self):
        print(f"Your balance = {self.balance}")


accounts: List[Bank] = []

while True:
    print("\n1. Add account")
    print("2. Display all accounts")
    print("3. Search account")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. Exit\n")
    choice = int(input("Enter choice = "))
    if choice == 1:
        x = Bank()
        accounts.append(x)
        print(accounts)
    elif choice == 2:
        for obj in accounts:
            obj.display()
    elif choice == 3:
        search_acc = int(input("Enter account number to search = "))
        exists = False
        for obj in accounts:
            if obj.account_number == search_acc:
                obj.display()
                exists = True
                break
        if not exists:
            # if exists==False:
            print("Account number does not exists")


    elif choice == 6:
        break
    else:
        print("Invalid Choice")


#Complete with Withdraw 
        
import random


class Bank:
    def __init__(self) -> None:
        self.account_number = random.randint(100000, 999999)
        self.holder = input("Enter your name: ")
        self.balance = 0.0
        self.account_type = input("Enter account type: ")

    def display(self):
        print(f"\nAccount number = {self.account_number}")
        print(f"Account holder = {self.holder}")
        print(f"Account balance = {self.balance}")
        print(f"Account type = {self.account_type}\n")

    def withdraw(self, amt: float):
        # amt = float(input("Enter amount to withdraw: "))
        if amt < 0:
            print("invalid amount")
            return
        if self.balance >= amt:
            self.balance -= amt
            print(
                f"amount {amt} has been debited from {self.account_number}. updated balance: {self.balance}"
            )
        else:
            print("Insuffcient balance")

    def deposit(self, amt: float):
        # amt = float(input("Enter amount to deposit: "))
        if amt < 0:
            print("invalid amount")
            return
        else:
            self.balance += amt
            print(
                f"amount {amt} has been credited to {self.account_number}. updated balance: {self.balance}"
            )

    def getBalance(self):
        print(f"Your balance = {self.balance}")


# b1 = Bank()
# b1.display()
# b1.deposit()
# b1.display()
# b1.withdraw()
# b1.display()

accounts: List[Bank] = []

while True:
    print("\n1. add account")
    print("2. display")
    print("3. search account")
    print("4. deposit")
    print("5. withdraw")
    print("6. transfer")
    print("7. exit\n")
    choice = int(input("Enter choice = "))
    if choice == 1:
        x = Bank()
        accounts.append(x)
        print(accounts)
    elif choice == 2:
        for obj in accounts:
            obj.display()
    elif choice == 7:
        break
    elif choice == 3:
        search_acc = int(input("enter acc. number to search = "))
        exists = False
        for obj in accounts:
            if obj.account_number == search_acc:
                obj.display()
                exists = True
                break
        if not exists:
            print("account number doesn't exist")
    elif choice == 4:
        search_acc = int(input("enter acc. number to search = "))
        exists = False
        for obj in accounts:
            if obj.account_number == search_acc:
                amt = float(input("enter amount to deposit: "))
                obj.deposit(amt)
                exists = True
                break
        if not exists:
            print("account number doesn't exist")
    elif choice == 5:
        search_acc = int(input("enter acc. number to search = "))
        exists = False
        for obj in accounts:
            if obj.account_number == search_acc:
                amt = float(input("enter amount to withdraw: "))
                obj.withdraw(amt)
                exists = True
                break
        if not exists:
            print("account number doesn't exist")
    elif choice == 6:
        account1 = int(input("enter your account number: "))
        account2 = int(input("enter recipients account number: "))
        amt = float(input("enter amount to be transferred: "))
        valid_acc = False
        for i in accounts:
            if i.account_number == account1:
                for j in accounts:
                    if j.account_number == account2:
                        if i.balance < amt:
                            print("Insuffcient balance")
                            break
                        i.withdraw(amt)
                        j.deposit(amt)
                        valid_acc = True
                        print(
                            f"amount of {amt} successfully transferred from {i.account_number} to {j.account_number}"
                        )
                        break
        if not valid_acc:
            print("enter valid details")

    else:
        print("invalid choice")
