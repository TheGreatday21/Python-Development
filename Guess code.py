##Using a function random to generate a random number
import random
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
    
    if guess < secretnumber :
        print("Your guess is too low")
    elif guess > secretnumber :
        print("Your guess is too high")
    else :
        break
if guess ==  secretnumber:
    print(f"Horray  you did it, you guessd the number in {guessesTaken} guesses")
else :
    print(f"Nope. The number i was thinking was {secretnumber}")


















