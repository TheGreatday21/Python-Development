import sys #this stands for system 

''''sys.argv''' #this stands for argument vector 
#this gets a list of all the arguments typed by the user at the prompt 
#catch all the documentation at 
''' docs.python.org/3/library/sys.html '''

'''
#the argv function is getting the first input placed in the terminal when running the program by the user 
print("hello, my name is ",sys.argv[1])
#we take the 1st argument because the arg at 0 is the name of the program 
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


#to perfect the error handling we can add an if statement to determine when the user puts in too many arguments 
if len(sys.argv) < 2: #if the arguments are less than 2
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is ",sys.argv[1])
#this is a more refined way to inform the user that more args are needed







