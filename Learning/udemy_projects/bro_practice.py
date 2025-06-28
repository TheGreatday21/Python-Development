'''
#Shopping list calculator

items = input("What do you want to buy?:\n")
quantity = int(input("How many items are you purchasing?:\n"))
price = float(input("How much is one item?($):\n"))

total = quantity*price

print(f"\nYou are buying {quantity} x {items}/s\n ")
print(f"\nYour total expenditure is {total:2} $\n")

print("\t\t\tThanks for using Finance pal\t\t\t\n\n")


#fibonacci practice ..
def fib(n):
    a = 0
    b = 1
    c = a + b
    list = []
    for i in range(0,n+1):
        i +=1 
        list.append(a)     
        a = b
        b = c
        c = a+b
    print(list)
fib(8)

#using augmented  assignment operators 
friends = 100

friends **= 2
print(f"This is exponents {friends}") 
friends *= 2
print(f"This is multiplication {friends}") 
friends += 12
print(f"This is addition {friends}") 
friends /= 2
print(f"This is division {friends}") 
friends %= 2
print(f"This is remainder after division {friends}") 

'''

#using the inbuilt math function 
'''
import math 

x= 9.9

# pi 
print(math.pi)
#exponents
print(math.e)
#square root
result = math.sqrt(x)
print(result)
#ceil - rounds a floating point number up 
result = math.ceil(x)
print(result)
#floor - rounds a number down 
result = math.floor(x)
print(result)


#Circumference
radius = float (input("Enter the radius of the circle (cm):"))
circumference = 2  * math.pi * radius
print(f"The circumference is : {round(circumference,2)}cm")


#Area 
radius = float (input("Enter the radius of the circle (cm):"))
area = math.pi * pow(radius, 2)
print(f"The area of the circle is : {round(area,2)} cm")

#Hypotenus
a = float(input("Enter Side A (cm) :"))
b = float(input("Enter Side B (cm) :"))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Side C = {c}")
'
'
##IF  statements
## Else do something else
age = int (input("Enter your age here ? :"))

if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print("You are now signed up !")
elif age < 0:
    print("You havent been born yet lol 😭")

else:
    print("You must be 18 + to sign up ")

#Example 2
response = input("Would you like food? (Y/N) :")

if response == "Y":
    print("Have some food ")
elif response == "N":
    print("No food for you ")
elif response == "":
    print("You did not enter a response nigaaa ")



##Using boolean variables 
for_Sale = True
if for_Sale:
    print("This item is for sale ")
else:
    print("This item is NOT for sale")

'''

'''
##PYTHON CALCULATOR
operator = input ("Enter an operation (+ - * /) :")
num1 = float(input("Enter the 1st number :"))
num2 = float(input("Enter the 2nd number :"))

if operator == "+":
    result = num1 + num2
    print(round(result,2))
elif operator == "-":
    result = num1 - num2
    print(round(result,2))
elif operator == "/":
    result = num1 / num2
    print(round(result,2))
elif operator == "*":
    result = num1 * num2
    print(round(result,2))
else:
    print(f"{operator} is not valid operator ")


## WEIGHT CONVERTER PROGRAM
weight = float(input("Enter your weight "))
unit = input("Kilograms or Pounds ? (K or L) : ")

if unit  == "K":
    weight = weight  * 2.205
    unit = "Lbs"
    print(f"Your weight is : {round(weight,1)} {unit}")
elif unit == "L":
    weight = weight  / 2.205
    unit = "Kgs."
    print(f"Your weight in {unit} is : {round(weight,1)} {unit}")
else:
    print(f"{unit} was not valid")




##TEMPERATURE CONVERSION PROGRAM

unit = input("Is this temperature in Celsius or Fahrenheit (C /F) :")

temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round ((9 * temp) / 5 + 32 ,1)
    print(f"The temperature is Fahrenheit is : {temp} ◦F ")
elif unit == "F":
    temp = round ((temp - 32)*5 / 9 ,1)
    print(f"The temperature is Celcius is : {temp} ◦C")
else:
    print(f"{unit} is an invalid unit of measurement ")

'''
'''
####LOGICAL OPERATORS .
# or - atleast one condition must be True
#and - both conditions must be true 
#not - is not false and not true

                                ##or operator
temp = 32
is_raining = False

if temp > 100 or temp < 0 or is_raining:#is the temperature greater than 100 and is it TRUE that it is raining 
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")



                    ##AND
temp = -10
is_sunny = False

if temp >= 28 and is_sunny:
    print("it is HOT outside 🥵🥵")
    print("It is SUNNY 🌞🌞")
elif temp <= 0 and is_sunny:
    print("It is COLD outside 🥶🥶")
    print("It is SUNNY 🌞🌞")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside 🌝🌝") 
    print("It is SUNNY 🌞🌞")
elif temp >= 28  and not is_sunny:
    print("It is HOT  outside 🥵🥵") 
    print("It is SUNNY 🌞🌞")

                ##NOT
if  temp <= 0 and not is_sunny:
    print("It is COLD outside 🥶🥶") 
    print("It is CLOUDY ☁️☁️")
elif 28 > temp > 0 and not is_sunny:
    print("It is WARM outside 🌝🌝") 
    print("It is CLOUDY ☁️☁️")
'''
'''

                        ##TENERAY OPERATORS/CONDITIONAL EXPRESSION
#A one line shortcut to if else statement 
#                   #x if condition else y
a = 4
b = 2
age =5
user_role = "admin"
num = 10

print("Positive" if num > 0 else "Negative")
result = "Even" if num%2 == 0 else "Odd "
min_num = a if a < b else b
max_num = a if b > a  else a
status = "Adult" if age >=18 else "Child"
access_level = "Full access" if user_role == "admin" else "Accessdenied"
print(access_level)



                        ####USER INPUT 
name = input("Enter your fullname:")
phone_number = input("enter your phone number (-):")
result = len(name)#get the length of a string 
result_1 = name.find(" ")#find is used to find the first occurrence of any character(index) ..In this case where space is 
result_2 = name.rfind(" e")#finding the last occurrence of a character 
capitalize = name.capitalize()#to capitalize the first letter of a string 
upper = name.upper()#to make all the input upper case 
lower = name.lower()#to make the input all lower case 
digit = name.isdigit()#to see if all the input is digital 
alphabet = name.isalpha()#is the input containing all alphabet characters
number = phone_number.count("-")
phone_number = phone_number.replace("-", "")

print(phone_number)

'''

####The metrix 

answr = input("What is your answer : Y or N ? ")

if answr == "Y":
    print("cant you see that i .... i ... you ~ Omah lay ")
else:
    print("I DONT ..... you  ")



























