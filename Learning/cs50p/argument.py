#creating a loop to take more args at the prompt 

import sys

if len(sys.argv) < 2:
    print("Too few arguments")
'''
for arg in sys.argv:
    print("Hey there ",arg)
#so here all the arguments are printed out including the name of the program
'''

#  so to correct this we can use a technique called slicing like in strings 
for argu in sys.argv[1:]: #give me elements from index 1 to whatever the user stops at 
    print(f"Hope your good {argu}") 















