#this is a simple rock paper scissors game 

import random


options = ('rock','paper','scissors')#creating a tuple with our options 
running = True#this boolean variable helps keep our code neat and easy to debug 

while running:

    player = None #no players yet 
    computer = random.choice(options) #using a function from the random library called choice that enables it chose from given options 
    #remaking the pc chose another random value     

    while player not in options:#the loop will continue if the user puts in something not into our options
        player = input("Enter a choice (rock,paper,scissors) : ")

    print(f"Player : {player} ")
    print(f"Computer  : {computer} ")


    if player == computer:
        print("Its a tie")
    elif player == "rock" and computer == "scissors":
        print("You win")
    elif player == "paper" and computer == "rock":
        print("You win")
    elif player == "scissors" and computer == "paper":
        print("You win")
    else:
        print("You loose")

    if not input("Play again? (y / n) : ").lower() == "y":#if the input is not y , then change the variable running to False and break out of the loop 
        running = False

print("Thanks for playing with me ")
    









































