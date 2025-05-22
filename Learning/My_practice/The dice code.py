#impirt library
import random
tries = 0
#create a function
def roll_dice_until_doubles():
    global tries  #declaringthe tries variable as a global variable
   
    doubles = False
    
    while not doubles:
        
        roll1= random.randint(1,6)
        roll2 = random.randint(1,6)
        
        print(f"Rolled {roll1} and {roll2}")
        
        tries += 1
        
        if roll1==roll2:
            print(f"Doubles in {tries} tries!")        
            doubles = True 
        
roll_dice_until_doubles()
        
        
        