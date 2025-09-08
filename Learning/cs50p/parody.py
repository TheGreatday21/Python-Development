#using the math conditionals 

def main():
    x = int(input("Place in a number to see if its even or odd :"))

    if x % 2 == 0:
        print("This is an even number")
    else:
        print("This is an odd number ")

#we can also use a function as a conditional in a loop 

    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    #we can collapse the four lines above into 1 line
    #return True if number % 2 == 0 else False >
    
    #The most logical way to do this is 
    #return number % 2 == 0 #the question it self has a true or false answer so you dont need to ask the question again 


main()