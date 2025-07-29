#python is an interpreted language unlike c which is a compiled language 
#there are alot of functions in python  . It was built to make work easier to easily solve problems 

name = input("What is your name? ")#getting input in form of strings 
#way one  - format
print(f"Hello, {name}")
#way two - concat 
print("Hello, " + name)
#way three - print one followed by the other
print("Hello,",name)



                        #python documentation can be found at  [docs.python.org]

#the print function comes with atleast 5 parameters 
#one is "sep = " and another is "end = " 
#we can overide these params to an thing we want to out put


print("Hello world", end = "! \n")


#simple python calc 

num1 = int(input("x: "))
num2 = int(input("y: "))
print(f"Your answer is {num1 + num2}")
#comparing strings in python is by using truthy like in js we donot need to use strcmpare like in c 


s = input("Do you agree? (Y or N): ")

if s == 'Y' or 'y':
    print("I am glad you agree with me ")
elif s == 'N' or 'n':
    print("Not agreed  ")

# we can also use the in key word . This helps us to tuckle more challenges at once 
if s in ["y","Yes","YeS","YEs","Y"]:
    print("Thanks for agreeing ")
elif s in ["N","n","No","NO"]:
    print("Not agreed ")



        #####   Object Oriented Programming 
#the oop (the use of objects ) in python is the equivalent of structs in c 

## when a function is associated to a specific data type it becomes a method 
#we can further simplify it to use a function 



t =  s.lower() #this is calling a method , cause lower is data type specific 
#we only need to place 2 params cause the function does all the conversion for us 
if t in ["y","yes"]:
    print("Thanks for agreeing ")
elif t in ["N","no"]:
    print("Not agreed ")


#you can also call method calls together 

favFood = input("What is your favorite food ?:").lower()
#this is calling 2 methods together which you can add more methods but you have to keep the code neat 

print(favFood)











