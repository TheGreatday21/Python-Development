''''
Kawooma Elijah 
B29158
Github: 

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
        
    def deposit(self,amount): #creating a method to allow depositing 
        if amount <= 0:
            print("Please input a sum greater than 0")
        else:
            self.balance += amount
            print(f"Your new balance is {self.balance} for account {self.account_number} under {self.name}")
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Account balance: {self.balance}")

#function to create an account 
def create_account(): 
    while True:
        userName = input("Name: ")
        
        try:
            userAccountNum = int(input("Account Num: "))
            break
        except (ValueError,TypeError):
            print("Please ensure the value is integer")
        except:
            print("Opps lets try that again")
        

def main():
    
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
        pass
    elif userInput == 3:
        pass
    elif userInput == 4:
        pass
    elif userInput == 5:
        pass
    elif userInput == 6:
        pass
    elif userInput == 7:
        sys.exit()


if __name__ == "__main__":
    main()
    
    

    
    
    