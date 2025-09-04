#these are things gone wrong in our code 

'''
print("hello world)

This dishes out a "syntax error" in the terminal - an error that involves wrong text input 

Another error is a runtime error mainly got when we get input from a user and they input somthing we didnot expect them to put in ; Like if we ask for an integer and they input a string 

'''
'''
x = int(input("What's x:"))
print(f"x is {x}")

What's x:rer
Traceback (most recent call last):
  File "D:\Elijah\languages_practice\Python\Learning\cs50p\exceptions.py", line 12, in <module>
    x = int(input("What's x:"))
ValueError: invalid literal for int() with base 10: 'rer'

We get a value error here , cause the user input a string instead of an integer . We would get the same thing even with a decimal and boolean value 

'''
#the best way to catch errors in python is using the try and except clause 
try:
    x = int(input("What's x:"))
    print(f"x is {x}")
except ValueError:
    print("You have to input an integer")

#there is a way to catch all the errors at once but it is bad practice to handle all of them in one go rather discover the errors and handle them as above 
'''
#here we are going to get the "Name error" cause the value error is happening too soon and the value is not copied to x 
try:
    x = int(input("What's x:"))
except ValueError:
    print("X must be an integer")

print(f"x is {x}")

What's x:re
You have to input an integer
What's x:re
X must be an integer
Traceback (most recent call last):
  File "D:\Elijah\languages_practice\Python\Learning\cs50p\exceptions.py", line 38, in <module>
    print(f"x is {x}")
                  ^
NameError: name 'x' is not defined

'''
#to fix the above error, we use an else statement with the try vlause
try:
    x = int(input("What's x:"))
except ValueError:
    print("X must be an integer")
else: #this code will only be run if you try above and succeed but if you donot , it stops at the exceptions . The print wont just run like it was before
    print(f"x is {x}")

#we got the name error because after solving the ValueError we just print but now x has no valid value hence the error pops up 

#to make this better we can use a loop to run it


while True:
    try:
        x = int(input("What's x:"))
    except ValueError:
        print("X must be an integer")
    else:
        break#if the user puts in the correct thing we break out the infinite loop 
#and print the value stored in x cause the else can only be run if the try was a success     
print(f"x is {x}")


#if we donot want to type anything in the exception we can use the pass key word
while True:
    try:
        x = int(input("What's x:"))
        break#break out of the loop if the user inputs the right thing 
    except ValueError:
        pass 
print(f"x is {x}")






