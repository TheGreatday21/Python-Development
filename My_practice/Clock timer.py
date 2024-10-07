
import time #first import the time library
def countdown(seconds):#create a function to do the counting
    print("Get ready , set , goooo")
    while seconds > 0:
        print(f"T-minus : {seconds}")
        seconds -=1#to tell python that thetime is to be reducing 
        time.sleep(1)#telling python to count in intervals of one second
    print("Lettssss gooooo, you did it")
print("ENTER YOUR PLANK DURATION IN SECONDS")
seconds = int(input())# create a variable fo users input
countdown (seconds) # countdown is a function
