#this is a program that just says hello to a user based on their input 

def main():
    name = input("What is your name: ")
    print(hello(name)) #print out the return value from the function 

def hello(to = "world"): # a function hello with a default value of world 
    return f"Hello,{to}"



if __name__ == "__main__":
    main()