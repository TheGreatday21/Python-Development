''''
for x in range(4):
    print("Happy birthday to me")
print("Nice going")

#calling a function inside a function

def main():
    print("I have a message for you")
    message()#defined the variable in a function
    print("Goodbye")
def message():
    print("The password is foo")
    
main()

##Example 2
def new():
    her= 1000
    print("NY" ,her, "consoles")
def old():
    her = 3000
    print("WH",her,"Love problems")
new()
old()

x = pow(4,5)##4 to the power 5
print(f"i have {x} bags and i love u")

##Example 3
def rec(num):
    print(num**2)
rec(78)

##having multiple arguments in a single function
def tie(num1,num2,num3):
    sum = num1 +num2 + num3
    print(f"The sum of the numbers is {sum}")
    average = sum/3
    print(f"There average is {average}")
tie  (23,90,45)
   
##Global variables and functions
name = "Opio john" 

def tree():
    print(f"Your name is {name}")
tree()   

###Inorder to change a global variable inside a function, you first have to inform python about it
name = "Afooyo Micheal"

def tree():
    global name
    name = "cock zuker"
    print(f"Arent you the famous {name}")
tree()
name = "Afooyo Micheal"

print(f"Cause i thought your actual name was {name}")

###Return statements.

def Recta(length,width):
    area = length *width
    return area
Recta_area = Recta(23,31)
print(f"The area of a rectangle is {Recta_area} squared centimeters")

##Example 1
def age(num1,num2):
    sum = num1 + num2
    return sum
my_age = age(23,24)
print(f"SO your total age is {my_age}")

def test():
    x = 8
    y = 7
    return x,y
p,q = test()
print(f"{p} loves {q}")
'''


































    
    
    
    
    
    
    
    
    
    
























