''''
Kawooma Elijah 
B29158

'''
# Objective
# You've been tasked by a local bank to create a simple bank account manager
# that can perform basic operations like deposit, withdrawal, and balance check.
# Use Object-Oriented Programming (OOP) to accomplish this.

import sys

class Banking:#creating a class with its methods to handle the operations 
    def __init__(self,name,account_number,balance =0): #placing the balance as a keyword argument incase a user doesnt input any balance when creating an account 
        self.name = name
        self.balance = balance
        self.account_number = account_number
        self.transactions = [] #creating a list to store the number of times we carryout any transaction
        
    def deposit(self,amount): #creating a method to allow depositing 
        self.balance += amount
        self.transactions.append(f"You deposited {amount}")
        print(f"Your new balance is {self.balance} for account {self.account_number} under {self.name}")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrew {amount}")
            print(f"Withdrew {amount} from account {self.account_number}, new balance: {self.balance}")
        else:
            print("Insufficient funds.")
            self.transactions.append(f"Failed withdrawal of {amount}")

    def check_balance(self):
        print(f"{self.name} your account balance is : {self.balance}")

    def transact_history(self): #creating method that will show/return contents from the transactions list for a given object
        if self.transactions:
            print(f"These are the transactions for {self.name}")
            for trans in self.transactions:
                print(trans, end="***")
        else:
            print("You havent done any transactions yet")
            
    def interest_rate(self,rate):
        self.rate = rate
        
        if rate <=0 :
            print("Invalid rate applied")
            
        else:
            interest = self.balance * (rate/100) #dividing the rate by 100 since its a percentage rate 
            self.balance += interest #the balance will increase by the interest
            self.transactions.append(f"You have recieved a {rate}% interest rate,your interest is {interest} and your current balance is {self.balance}")
            print(f"Account {self.account_number} under {self.name} recieved an interest of {interest} at rate{self.rate}.  New account balance is {self.balance}")





bank_accounts = {}#creating an empty dictionary to store all the accouts
#bank_accounts_names = {}#creating a dictionary for all the account holders names 

#function to create an account 
def create_account(): 
    while True:
        try:
            userName = input("Name: ")
            userAccountNum = int(input("Account Num: "))
            if userAccountNum in bank_accounts:
                print("Account number already exists! Try a different number.")
                continue
            bank_accounts[userAccountNum] = Banking(userName, userAccountNum)
            #bank_accounts_names[userAccountNum] = userName #using the account num as the key and name as the value 
            print(f"Account created successfully for {userName} with account number {userAccountNum}")
            break
        except (ValueError, TypeError):
            print("Please ensure the account number is an integer.")
        except:
            print("Oops, let's try that again.")

#function to deposit money
def deposit_money():
    try:
        userAccountNum = int(input("Account Num: ")) #function should check dictionary to see the user account num then proceed 
        account = bank_accounts.get(userAccountNum)
        if account:
            amount = float(input("Amount to deposit:"))
            account.deposit(amount)
        else:
            print("Account not found.")
    except ValueError: #any input thats not integer or float will be captured here
        print("Account number must be integer . Invalid deposit ")
             
#function to check account balance         
def check_balance():
    try:
        userAccountNum = int(input("Account Num: ")) #function should check dictionary to see the user account num then proceed 
        account = bank_accounts.get(userAccountNum)
        if account:
            account.check_balance()
        else:
            print("Account not found.")
    except (ValueError,TypeError):
        print("Please ensure the value is integer")

#creating a function to withdraw
def withdraw():
    try:
        userAccountNum = int(input("Account Num: "))
        account = bank_accounts.get(userAccountNum) #checking the dictionary to see if the account num exists 
        if account:#if true update the details of that object 
            amount = float(input("Amount to withdraw: "))
            account.withdraw(amount)
        else:
            print("Account not found.")
    except ValueError:
        print("Invalid input. Amount and account number must be numbers.")

#creating a function to get the transaction history 
def transaction_history():
    try:
        userAccountNum = int(input("Account Number: "))
        account = bank_accounts.get(userAccountNum)
        if account:
            account.transact_history()
        else:
            print("Account not found.")
    except ValueError:
        print("Invalid input. Account number must be an integer.")

#creating a function to give interest
def interest():
    try:
        userAccountNum = int(input("Account Num: ")) #function should check dictionary to see the user account num then proceed 
        account = bank_accounts.get(userAccountNum)
        if account:
            rate = 10 #harcoding the rate so that every account automatically gets a 10 %interest rate 
            account.interest_rate(rate)
        else:
            print("Account not found.")
    except ValueError: #any input thats not integer or float will be captured here
        print("Invalid input. Account number must be numbers.")


def main():
    while True:
        print("\n")
        print("1. Create new account:")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer to other account")
        print("5. Check balance")
        print("6. Transaction History")
        print("7. Exit")
        while True:
            try:
                userInput = int(input("\n Chose an operation: "))
                break
            except (ValueError,TypeError):
                print("Please input the right data ")
        
        
        if userInput == 1:
            create_account()
        elif userInput == 2:
            deposit_money()
        elif userInput == 3:
            pass
        elif userInput == 4:
            pass
        elif userInput == 5:
            check_balance()
        elif userInput == 6:
            transaction_history()
        elif userInput == 7:
            sys.exit()
        else:
            print("Ïnvalid option ")

if __name__ == "__main__":
    main()
    
    

    
    
    