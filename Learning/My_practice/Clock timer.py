
import time #first import the time library
def countdown(seconds):#create a function to do the counting with the seconds variable as an argument 
    print("Get ready")
    time.sleep(2)
    print("set ")
    time.sleep(2 )
    print("goooo")

    while seconds > 0:
        print(f"T-minus : {seconds}")
        seconds -=1#to tell python that thetime is to be reducing 
        time.sleep(1)#telling python to count in intervals of one second
    print(f"Lettssss gooooo, you did it")


while True:
    print("ENTER YOUR PLANK DURATION IN SECONDS")
    seconds = int(input())# create a variable fo users input
    countdown (seconds) # countdown is a function
    print(f"You planked for {seconds} seconds total ")
