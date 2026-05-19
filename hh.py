class ATM:
    def __init__(self):
        self.name = "Geetha"
        self.gmail = "geetha@gmail.com"
        self.password = 1234
        self.balance = 10000
        self.accountnumber = 987654321


# Custom Exception
class ATMError(Exception):
    pass


class Operations(ATM):

    def balanceenquiry(self):
        print("Current balance is:", self.balance)

    def cashdeposit(self):
        try:
            amount = int(input("Enter deposit amount: "))

            if amount <= 0:
                raise ATMError("Deposit amount should be greater than 0")

            self.balance += amount

            print("Amount deposited successfully")
            print("Updated balance is:", self.balance)

        except ATMError as e:
            print(e)

        except ValueError:
            print("Please enter numbers only")

    def cashwithdrawl(self):
        try:
            amount = int(input("Enter withdraw amount: "))

            if amount > self.balance:
                raise ATMError("Insufficient balance")

            self.balance -= amount

            print("Withdrawal successful")
            print("Remaining balance is:", self.balance)

        except ATMError as e:
            print(e)

        except ValueError:
            print("Please enter numbers only")

    def changepassword(self):
        try:
            oldpassword = int(input("Enter old password: "))

            if oldpassword == self.password:

                newpassword = int(input("Enter new password: "))
                self.password = newpassword

                print("Password changed successfully")

            else:
                print("Old password is incorrect")

        except ValueError:
            print("Password should contain numbers only")

    def emailchecking(self):
        try:
            email = input("Enter your email: ")

            if email != self.gmail:
                raise ATMError("Email is incorrect")

            print("Email verified successfully")

        except ATMError as e:
            print(e)

    def exit(self):
        print("Thank you for visiting ATM")


# Object Creation
obj = Operations()


# Login System
attempts = 0
max_attempts = 3

while attempts < max_attempts:

    try:
        userpassword = int(input("Enter password: "))
        username = input("Enter username: ")

    except ValueError:
        print("Password should contain numbers only")
        continue

    if username == obj.name and userpassword == obj.password:

        print("\nLogin Successful\n")

        while True:

            try:
                choi = int(input(
                    "\n1. Balance Enquiry\n"
                    "2. Deposit\n"
                    "3. Withdraw\n"
                    "4. Change Password\n"
                    "5. Email Verification\n"
                    "6. Exit\n"
                    "Enter your choice: "
                ))

                match choi:

                    case 1:
                        obj.balanceenquiry()

                    case 2:
                        obj.cashdeposit()

                    case 3:
                        obj.cashwithdrawl()

                    case 4:
                        obj.changepassword()

                    case 5:
                        obj.emailchecking()

                    case 6:
                        obj.exit()
                        break

                    case _:
                        print("Invalid choice")

            except ValueError:
                print("Please enter numbers only")

        break

    else:
        attempts += 1

        print("Invalid username or password")
        print("Remaining attempts:", max_attempts - attempts)


if attempts == max_attempts:
    print("\nYou crossed maximum login attempts")
    print("Your account is temporarily blocked")