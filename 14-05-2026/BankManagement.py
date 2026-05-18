class Bank:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount Deposited {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient Funds")
        self.balance -= amount
        print(f"Amount Withdrawn {amount}")

    def view_balance(self):
        print("Current Balance:", self.balance)

class LessDepositAmountError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

class WrongCredentialsError(Exception):
    pass

def enter_bank():
    chances = 3
    access = False
    while chances > 0:
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        try:
            if username != "admin" or password != "1234":
                raise WrongCredentialsError("Invalid Credentials")
            access = True
            print("Login Successful")
            break
        except WrongCredentialsError as e:

            chances -= 1
            print(e)
            if chances > 0:
                print(f"{chances} chances left")
    if not access:
        print("Account Blocked")
        return
    obj = Bank(0)

    while True:

        print("""
1.Deposit
2.Withdraw
3.View Balance
4.Exit
""")
        try:
            op = int(input("Enter your choice: "))
            match op:
                case 1:
                    amt = int(input("Enter deposit amount: "))
                    obj.deposit(amt)
                case 2:
                    amt = int(input("Enter withdraw amount: "))
                    obj.withdraw(amt)
                case 3:
                    obj.view_balance()
                case 4:
                    print("Thank You")
                    exit()
                case _:
                    print("Invalid Choice")

        except ValueError:
            print("Enter valid number")

        except InsufficientFundsError as e:
            print(e)

        except Exception as e:
            print(e)

enter_bank()