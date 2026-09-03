class Transaction:
    #Constructor
    def __init__(self, amount:float, transaction_type:str):
        self.transaction_type=transaction_type
        self.amount= amount
        
class Account:
    #Constructor
    def __init__(self, account_number:int, holder_name:str, balance:float=0):
        self.account_number=account_number
        self.holder_name=holder_name
        self.balance = balance
        self.transactions = []
    #Deposit amount in account and save a register in transactions    
    def deposit(self,amount:float):
        if amount > 0:
            self.balance += amount
            self.transactions.append(Transaction(amount,"Deposit"))
            print(f"Deposit of ${amount} successful. \nNew balance is ${self.balance}")
        else:
            print("Invalid deposit amount.")
    #Withdraw amount from acount and save a register in transactions 
    def withdraw(self, amount:float):
        if 0 < amount <=self.balance:
            self.balance -= amount
            self.transactions.append(Transaction(amount,"Withdraw"))
            print(f"Withdraw of ${amount} successful. \nNew balance is ${self.balance}. ")
        else:
            print("Invalid withdraw amount")
    #Get transactions register        
    def display_transaction(self):
        print("Transaction History:\n ")
        for transaction in self.transactions:
            print(f"${transaction.amount}  {transaction.transaction_type}")
    #Get account balance        
    def display_balance(self):
        print (f"Current balance for account {self.account_number}: ${self.balance}")    
        
class Bank:
    #Constructor
    def __init__(self, name:str):
        self.name=name
        self.accounts={}
    #Create an account, validate the account dont exist and save number account in accounts
    def create_account(self, account_number:int, holder_name:str, initial_balance:float=0):
        if account_number not in self.accounts:
            new_account = Account(account_number, holder_name, initial_balance)
            self.accounts[account_number]=new_account
            print(f"Account was created successful for {holder_name}. \nAcount number is {account_number}")
        else:
            print("Account with the given number already exist.")
    #Get number account         
    def get_account(self, account_number:int):
        return self.accounts.get(account_number)
#Instantiate a bank    
bank=Bank("Colptria")
#Instantiate accounts
alice_account = bank.create_account(123456,"Alice",200)
bob_account = bank.create_account(234567,"Bob")
#Get numbers account
alice_account_number = bank.get_account(123456)
bob_account_number= bank.get_account(234567)
#Deposit and withdraw = just use functions
alice_account_number.deposit(1000.0)
alice_account_number.withdraw(200)
bob_account_number.deposit(600)
bob_account_number.withdraw(500)
alice_account_number.display_transaction()
alice_account_number.display_balance()