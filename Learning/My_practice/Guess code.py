##Using a function random to generate a random number
import random
##Using a function math 
import math

##Generate a random nuber between 1 and 20
secretnumber= random.randint(1,20)

print("Welcome to my game of guesses")
print("Think of a number between 1 and 20")
#Declare integer variable to store number of guess
guessesTaken = 0


#Give the guest a bout 6 chances to guess
for guessesTaken in range(1,7):
    print("Please take your first guess :")
    guess = int(input())
    is_number = not guess.is_integer() 
    if is_number :
        print("Wrong input amigo")
        break
    else:
        
        if guess < secretnumber :
            print("Your guess is too low")
        elif guess > secretnumber :
            print("Your guess is too high")
        elif guess ==  secretnumber:
            print(f"Horray  you did it, you guessd the number in {guessesTaken} guesses")
        else:
            print("Try again next time")
        break
    
else :
    print(f"Nope. The number i was thinking was {secretnumber}")


















