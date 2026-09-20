# Errors --> an issue that disrupts normal execution of program
# Exception --> Error

# IndentationError
# IndexError
# AssertionError
# AttributeError
# ImportError
# KeyError 
# NameError
# MemoryError
# TypeError

# Exception handling = Control the crash

# try: 
#     ## Code
# except: 
#     ## Code

# try:
#     num = int(input("Enter Number: "))
#     result = 10/num
# # except ZeroDivisionError:
# #     print("cannot devide by zero")
# # except ValueError:
# #     print("Invalid Input")
# except (ZeroDivisionError, ValueError):
#     print("Invalid Operation")

# else: 
#     print("Result: ", result)

# finally: 
#     print("Welcome to Technogeeks")

# Raise Exception 

## user defined exceptions

# class InvalidVoter(Exception):
#     pass



# age = int(input("Enter Age: "))

# if age < 18:
#     raise InvalidVoter("Not eligible for voting")



# try:
#     num = int(input("Enter Number: "))
#     result = 10/num

# except Exception as e:
#     print("Error: ", e)

class InvalidAmountError(Exception):
    pass
class InsufficientBalance(Exception):
    pass

class InvalidChoice(Exception):
    pass

class BankAccount: 
    
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):

        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be greater than 0")
        
        self.balance += amount
        print("Deposited: ", amount)

    def withdraw(self, amount): 
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be greater than 0")
        
        if amount > self.balance:
            raise InsufficientBalance("Not Enough Balance")
        
        self.balance -= amount
        print("Withdrawn: ", amount)

    def check_balance(self):
        print("Current Balance: ", self.balance)
            

account = BankAccount(1000)

try: 
    print("1. Deposit")
    print("2. Withdraw")

    choice = int(input("Enter Choice: "))
    if choice not in [1, 2]:
        raise InvalidChoice("please choose from 1 or 2")
    amount = int(input("Enter Amount: "))

    if choice == 1:
        account.deposit(amount)

    elif choice == 2:
        account.withdraw(amount)

    else: 
        print("Invalid Choice")

except ValueError as e:
    print("InvalidInput: You need to enter numbers only.")

except InvalidAmountError as e:
    print("Error: ", e)

except InsufficientBalance as e:
    print("Error: ", e)
    
finally: 
    print("Transcation Completed")
    account.check_balance()