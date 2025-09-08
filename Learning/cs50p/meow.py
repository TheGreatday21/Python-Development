def main():
    number = getNumber()
    meow(number)

def getNumber():
    #we error handle at this point if a user is to put in something contrary to an integer 
    while True:
        n = int(input("What is your n: "))
        if n > 0:#keep looping if the users number is lesser than 0
            break
    return n

def meow(n):
    for _  in range(n):    
    #placing this in the range of the input
        print("meow")



main() 