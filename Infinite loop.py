##Using a function random to generate a random number
import random

##Generate a random nuber between 1 and 20
secretnumber= random.randint(1,20)

print("Welcome to my game of guesses")
print("Think of a number between 1 and 20")
#Declare integer variable to store number of guess
guesses = 0
guess = 0
#Give the player infinite guwessing using  w hile  loop while the guess is not true
while guesses != secretnumber:
    print("Take a guess")
    guess = int(input())

    guesses += 1
    
    if guess < secretnumber :
        print("Your guess is too low")
    elif guess > secretnumber :
        print("Your guess is too high")
    else :
        break
if guess ==  secretnumber:
    print("Horray  you did it, you guessd the number in",+str(guessesTaken)+ "guesses")
else :
    print("Nope. The number i was thinking was ",+str(guess))

    
    
    
    