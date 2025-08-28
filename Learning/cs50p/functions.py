def main(): #defining my main function like in any programming language that matters 
    name = input("What's your name? ").title()
    hello(name)#calling the function with the parameter i added to the function 
    hello()



def hello(aName = "user" ): #user becomes the default value for the parameter in our function
 #we can add a default value here like on the named params of the print function
    print(f"Hello there {aName}")

#python has no prototyping but we organise our functions in the main function and call it at the end of our file 





main()