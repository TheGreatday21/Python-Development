##this is a package iam going to use in my code originally 
def main():
    hello("world")
    goodbye("world")

def hello(name):
    print("Hello,",name)
def goodbye(name):
    print("Good bye",name)

if __name__ == "__main__": #this stops us from calling main unnecessarily
    main()