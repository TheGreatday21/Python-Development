#creating a program where a function returns a value 
def main():
    x = int (input("Number here: "))
    print(f"{x} squared is ",square(x))

    y = int (input("Number here: "))
    print(f"{x} to the power {y} is ",toThePower(x,y))

def square(num): #creating a function that takes in a number arg and mulitiplies it by it self 
    return num*num


def toThePower(number,valuePower):
    return pow(number,valuePower) #or you can use this syntax
    #return number ** valuePower

main()