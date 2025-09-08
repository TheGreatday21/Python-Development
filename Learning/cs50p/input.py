#this is a program that takes user input and returns a value on the console for us 

name = input("What is your name? ")

print("Hello there ",name )
print(f"It's nice to meet you {name}")

#passing in some named params 
print("Are you from Ohio ", name , sep='-- ')#we are going to seperate them with a --

#####you can preceed the input function with a data type to get a specific type of data . The default is obviously a string 
age = int(input("How old are you ?"))
print(f"You are {age} years old")

print(float(input("How tall are you: ")))#we can also just directly print out what the user is typing in 


