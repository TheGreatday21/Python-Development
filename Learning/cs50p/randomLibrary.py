#this is code that you write to either share with others or use by yourself

#libraries in python are called "modules" 

#the most common modules are 
'''
random - for generating a random number 
docs.python.prg/3/library/random.html
'''

#to use a module we use the key word "import"
# import random 

# numbers = [3,5,2,1,6,9]
# random.choice(seq)#seq here is something like a list 


import random 

coin = random.choice(["heads","tails"]) #random.choice is a function that takes a list as an arg and returns the values with a 50/50 probability 
print(coin)


#when we want to import specific functions from a module we use the key word "from".The import brinds in everything from the module without specifying 
#so the improved statement will be 
from random import choice

#this is advantageuos if you only have to use that one function from the module 
dice = choice([1,2,3,4,5,6])
print(dice)

'''
another useful function is the randint function that returns a random integer and takes two args as the range 
'''

from random import randint

number = randint(1,10)#this generates a random number between 1 and 10
print(number)
#this can be used in simple programs like a guessing game or in changing the output of your code 


'''
another function is the shuffle function 
'''

from random import shuffle

cards = ["jack","queen","king"]

card = shuffle(cards)

for card in cards:
    print(card)
























































