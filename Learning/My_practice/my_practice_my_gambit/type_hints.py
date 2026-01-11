
def meow(n:int):
    for _ in range(n):
        print("meow")

#this is type hinting for variables 
number:int  = int(input("Number: "))
meow(number)


####we can use """ mypy""" to ensure our variables have the right type 

##we can use the arrow key to hint on the return value of a function

def sing(n:int) -> str: #this function returns a string 
    return "laaaaaaaa\n" * n

keks:str = sing(4)
print(keks,end = "")


