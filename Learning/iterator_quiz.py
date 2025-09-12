'''
#Given the code 
my_sentence = Sentence('This is a test ')

for word in my_sentence:
    print(word)

#this should return :
# This 
# is 
# a 
# test
'''

#using a generator 
def sentence(userInput):
    words = userInput.split()
    for text in words :
        yield text

my_sentence = sentence('This is a test')

for word in my_sentence:
    print(word,end='\n')

'''

#using a class
class Sentence:
    def __init__(self,sentence):
        self.sentence = sentence #creating a class attribute for the variable 
        self.index = 0 #this helps us keep track of where we are when iterating 
        self.words = self.sentence#this attribute contains all the individual strings in the sentence 

    def __iter__(self): #this method is created to make this class iterable 
        return self
    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration#if there are no more words 
        index = self.index #temporary variable starting at o 
        self.index += 1 #increasing the index 
        return self.words[index] #returning the word at that index 

my_sentence = Sentence('I love to eat rice and matooke')

for word in my_sentence:
    print(word,end=" ")

'''






































