#is like a list with no duplicates 


students = [{"name":"John","house":"Moroto"},
{"name":"Simon","house":"Elgon"},
{"name":"Peter","house":"Rwenzori"},
{"name":"Sandra","house":"Elgon"}
] #created a list of dictionaries 

# houses = []#initially using a list now shifting to use of a set

# for student in students:
#     if student["house"] not  in houses:
#         houses.append(student['house'])

# for house in sorted(houses):
#     print(house)

houses = set()
for student in students:
    houses.add(student['house'])

for house in sorted(houses):
    print(house)

#############################################################################################################

#global variable is a variable outside all your functions that cannot directly be changed inside the functions unless you make the global variable local 
#local variable is a function inside a function

balance = 0

def main():
    print(f"Balance: {balance}")
    deposit(100)
    withdraw(50)
    print(f"Balance: {balance}")

def deposit(n):
    global balance 
    balance += n

def withdraw(n):
    global balance 
    balance -= n

if __name__ == "__main__":
    main()


#################THE OOP IMPLEMENTATION OF THIS BANK SYSTEM 

class Account:
    def __init__(self):
        self._balance = 0 #this is a private attribute 
        #can be accessed by all the methods in the class unlike protected that cannot be accessed 
    
    @property #this is a getter 
    def balance(self):
        return self._balance

    
    def deposit(self,n):
        self._balance += n

##these donot need to be setters 
    
    def withdraw(self,n):
        self._balance -= n

def main():

    account = Account()

    print(f"Balance {account.balance}")

    account.deposit(100)
    account.withdraw(50)

    #account.balance = 300 #this wont work because a setter is not defined in the class

    print(f"Balance {account.balance}")



if __name__ == "__main__":
    main()