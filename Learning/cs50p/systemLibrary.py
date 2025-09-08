import sys #this stands for system 

''''argv''' #this stands for argument vector 
#when we call the function "sys.argv" it gets a list of all the arguments typed by the user at the prompt 
#catch all the documentation at 
''' docs.python.org/3/library/sys.html '''

'''
#the argv function is getting the first input placed in the terminal when running the program by the user 
print("hello, my name is ",sys.argv[1])
#we take the 1st argument because the arg at index 0 is the name of the program 
'''

#if we donot get user input we get an error 
'''
Traceback (most recent call last):
  File "D:\Elijah\languages_practice\Python\Learning\cs50p\systemLibrary.py", line 10, in <module>
    print("hello, my name is ",sys.argv[1])
                               ~~~~~~~~^^^
IndexError: list index out of range

'''

#using a try  except block to catch this error '
try :
    print("hello, my name is ",sys.argv[1])
except IndexError:
    print("You have to add a parameter before running the program ")


#to perfect the error handling we can use  an if statement to determine when the user puts in too many arguments 
if len(sys.argv) < 2: #if the arguments are less than 2. because arg 0 - name of program, arg 1 - arg from user.
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else: #if there are only two args ie 0 - name of program and 1 - user input 
    print("hello, my name is ",sys.argv[1])
#this is a more refined way to inform the user that more args are needed

#the only way we can view a full name is by placing multiple arguments in the same "" at the terminal
'''
PS D:\Elijapython .\systemLibrary.py "keks the great">
File "D:\Elijah\languages_practice\Python\Learning\cs50p\systemLibrary.py", line 10, in <module>
hello, my name is  keks the great
hello, my name is  keks the great
'''

#it is important to keep all the error handling seperate from the code that really matters to you
#here we will use the""" sys.exit """"  function


#check for errors
if len(sys.argv) < 2:
    sys.exit("Too few args at prompt")
elif len(sys.argv) > 2:
    sys.exit("Too many args at prompt")

#since sys.exit has been used, this line will only be reached if the correct arguments are placed in 
#print name tags here
print("Hey there ",sys.argv[1])











