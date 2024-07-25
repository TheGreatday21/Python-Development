#we are going to jumble words ie we are making a scrabble programm , it jumbles words and asks you for what the word is

#we use the random function
import random
#create a list
words = ['keks', 'john', 'simon']
word = random.choice(words)#you can pick an item from a list of items
print(word)

jumbled = list(word)#makes a list of characters from the random word it choses
print(jumbled)

random.shuffle (jumbled)
print(jumbled)
print("Unscrumble the letters  to make a word ", '' .join(jumbled))


#####let some one gues the word and confirm if it is correct.Give the a shout 
guess = input("Your Guess :\n")

if guess == word:
    print("Correct")
else:
    print("Incorrect")

















