#we are going to jumble words ie we are making a scrabble programm , it jumbles words and asks you for what the word is

#we use the random function
import random
#create a list
words = ['pineapple', 'john', 'simon']
word = random.choice(words)#tells python to pick any one word from the list
print(f"\n{word}\n")#and print it out

#Then after printing it out we told python to fetch that word and list it
jumbled = list(word)#makes a list of characters from the random word it choses
print(f"{jumbled}\n")#printing the listed word

random.shuffle (jumbled)#we use the random.shuffle function to randomize the word that was listed
print(jumbled)
print("Unscrumble the letters  to make a word ", '' .join(jumbled))


#####let some one gues the word and confirm if it is correct.Give them a shot 
guess = input("Your Guess :\n")
for word in words:
    if guess == word:# The word that was picked initially on random.choice
        print("Correct, you got it right")
    else:
        print("Incorrect,try again later")

















