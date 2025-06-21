#First function of the day 
print("Hello world you'll (: ")

'''
THIS IS A MULTI COMMENT .
'''
#Creating a dictionary 
words = set()

def check(word):
    return word.lower() in words


def load(dictionary):
    with open(dictionary) as file:
        words.update(file.read().splitlines())
    return True

def size():
    return len(words)

def unload():
    return True













