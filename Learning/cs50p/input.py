#this is a program that takes user input and returns a value on the console for us 

name = input("What is your name? ")

print("Hello there ",name )
print(f"It's nice to meet you {name}")

#passing in some named params 
print("Are you from Ohio ", name , sep='-- ')#we are going to seperate them with a --
