#python doesnot require the ; at the end of code lines like in c c++ and js

#First function of the day 
print("Hello world you'll (: ")

'''
THIS IS A MULTI COMMENT .
'''

#Creating a set , where no entries can be duplicated 
words = set()

def check(word):
    return word.lower() in words
#this returns a word in the set of words 


def load(dictionary):
    with open(dictionary) as file:
        words.update(file.read().splitlines())
    return True

def size():
    return len(words)

def unload():
    return True
#since python handles memory for you 












