#Creating  a program to help kids do math
#Asking the kids name first
name = input("        What is your name?: ")
print("           Hello ", name, "Today we will learn some maths ")
#asking the kid to input their 1st no and second number
print("Type in your first number ")
li = int(input())
#asking the child which operation they want to do first
print("1. +")
print("2. -")
print("3. /")
print("4. *")
print("Now, select 1 for addition, 2 for subtraction, 3 for division and 4 for multiplication")
#operator function for bodmas operations and storing it with the input function 
operator = int(input())
#asking for the second input
print("Now please type in your second number ")
zi = int(input())

#using if statements after the operator inputs 
#Addition
if operator== 1:
    print("What is ",li, "+" ,zi)
    di =li + zi

#Subtraction
if operator == 2:
    print ("What is ",li,"-",zi)
    di =li - zi
#Division
if operator == 3:
    print ("What is ",li,"/",zi)
    di =li / zi
#Multiplication
if operator == 4:
    print ("What is", li,"*",zi)
    di =li * zi

#Creating an input value for the users input
gi =int(input())

#Comparision of the answers with the pc    
if di == gi:
        print("Yiiiippiiiiiiiiiiiiii..... you did it",name, "thats coreect")
else:
        print("Thats wrong",name,"but the answer is", di)
        
        
        #in python we respect spacing and indentation , it affects how the code runs