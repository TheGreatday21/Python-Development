# we can use a method that tells us wether the user input is string or integer 

n = input("Input: ")
if n.isnumeric():
    print("Integer")
else:
    print("Is a string")



#an exception terminates a program 

#the try block of code requires less code 
try:
    number = int(input("A number:"))
    #print("Integer")
    #we have to reduce the number of lines of code in the try block of code 
except ValueError:
    print("Not integer")

else:#we can use an else statement with the try except close 
    print("Integer")



###### MARIO  ######
while True:#a cheap way to do a do while loop in python since it aint there . Deliberately infinitely looping 
    blocks = int(input("Height: "))
    if blocks > 0:
        break

for i in range(blocks):
    print("#") 

for i in range(blocks):
    print("?",end="") #to make it horizontal 
print()

#the print function can take calculations directly 
print("?" *4)

## getting a grid 

for i in range(blocks):
    for j in range(blocks):
        print("#", end="")
    print()

