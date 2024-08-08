''''
#2. Conditional Statements & Lists: # type: ignore
# Write a Python program that asks the user to input their grades for five different subjects. Store these grades in a list. 
#Then, use conditional statements to determine if the student has passed or failed. (Assume a passing grade is 50 or higher.)
#Print "Pass" if the student has passed all subjects, otherwise print "Fail." # type: ignore



A = int(input("What did you get in  Math : "))
B = int(input("What did you get in  Chemistry : "))
C = int(input("What did you get in  Physics : "))
D = int(input("What did you get in General Paper : ")) 
E = int(input("What did you get in  Computer studies : "))
D = [A,B,C,D,E]

print(D)

count = 0 
for num in D :
    if num < 50:
        count += 0
    else :
        count += 1
if count >=5:
    print("Congratulations nigga ,\n\t ....PASSED.....")
else:
    print("Iam sorry to say but try again next time, \n\t...FAILED...")


#3. Loops & Strings:
#At Uganda Christian University, students are assigned unique IDs consisting of the prefix "UCU" followed by a number (e.g., UCU12345). 
#Write a Python program that generates a list of 10 student IDs starting from "UCU10001" to "UCU10010" using a loop. 
# Then, print each ID on a new line.

for i in range (1,11):
    a = list((f"UCU100{i}"))
    print(a)



#4. Tuples, Sets, & Dictionaries:
#Uganda Christian University offers various programs in different faculties. 
# Create a tuple containing three faculties. For each faculty, create a set of three programs offered. 
# Finally, create a dictionary where the keys are the faculty names and the values are the corresponding sets of programs.
#  Write a Python program to display the programs offered in the "Faculty of Science and Technology."

faculty = ("Engineering","Masscommunication","Law")
Engineering = {"Data science", "Civil ", "Electrical"}
Masscommunication = {"Journalism","Field work","Radio presenting"}
Law = {"Criminal", "Land","Constitutional"}
dee = list[Engineering,Masscommunication,Law]

dictionary_one = {faculty : dee}#at this step we make the faculty values keys and the list dee values
#these are proof the keys and values are in sync with the question
dict_keys = dictionary_one.keys()
print(dict_keys)
###OR
for key in dictionary_one.keys():
    print(key)

dict_values = dictionary_one.values()
print(dict_values)
#the whole dictionary is
print(dictionary_one)


#python time counter
import time#import the time library
def plank(secs):#create a function that counts
    print("Alright less get it ")

    while secs > 0 :#use  a while loop to make the code loop
        print(f"Youare left with {secs}  seconds to go ")
        secs -= 1
        time.sleep(1)
a = int(input("Place in your plank time in seconds : "))
plank(a) 
print("Hurrayyyyy you did it .. less go again ")


string_text =  "Hello world!"
print(string_text[6:])#this calls all the letters from the sixth index of the string

string= "python is fun !"
print(string[::-1])#reverses the text literally


##getting multiples of 3 and 5 form user input number
numbers =  int(input("Type in any numeber here : "))
print(f"Your number is {numbers}\n")
for num in range(0,numbers +1):#create a for loop with a range to pick the numberes from
    if num % 3 == 0:#if the number in numbers has a zero remainder after division with 3
        print("Fizz")
    elif num % 5 == 0:#if the number in numbers has a zero remainder after division with 5
        print("Buzz")
    elif num % 3 == 0 and num % 5 ==0:#if the number in numbers has a zero remainder after division with both  3 and 5
        print("FizzBuzz")
    else:#if the number fills none of the above critea just print the number live and shit
        print(num)



## multiplication
import time
print("\n\tThis program will create a multiplication table for any number you input\n")
time.sleep(2)
multiplication = int(input("Input any number yuo want to get the multiplication for "))

for i in range(1,multiplication+1):
    print(f"{multiplication} * {i} = {multiplication * i}")
    time.sleep(1)
'''

##summation of all even numbers
number1 = int(input("Input number : "))
count = 0
for i in range(1,number1+1):
    if i % 2 ==0:
        print(i)
        count += 1
print(f"There are {count} even numbers in your number{number1}")















