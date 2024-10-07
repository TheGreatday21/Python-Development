''''
#variables store information from strings,integers,floats and boolean 
#they require an = sign to give value to the variable\
math = 2 + 4
subtract = 4 - 2
divide = 9/3   #divide gives us a float cause 9divide by 3 gives 3 remainder 0
divide2 = 9//3  #now this will just give us a whole number only
divide3 = 9%3 #now this gives us the remainder of when the two numbers divide each other

#When naming variables ... They cannot start with integers 
#2math = 3+4#this will give an error
#lar_khsd khd = 5+3#This will also bring an error because variables shouldnt contain spaces but rather an underscore

#We can also use f strings directly in variables
ABBS = "health"
weed = f"Weed is bad for your {ABBS}"
print(weed)

#to concatenate 2 strings we use the + sign but we cannot concatenate a string and an integer in a print statement unless the integer is turned into a string  or we use either an f string or commas
A = "I love Jesus"
B = " and he loved me first"
print(A+B)
C = 45
#print(B+C)#This brings an error so we convert c to str
print(B + str(C))#works cause we turned it to string


##for loops and while loops
#while loops are conditional
ann = int(input("How old are you ? "))
while ann <= 0:
    print("There is no way your below 0 years old ")
    ann = int(input("How old are you ? "))
while ann < 18:#creating another while loop linking to the first and an if else scenario after breaking out the while loop
    print("Ohhhh .. unfortuantely this site is for adults only, please try again  ")
    ann = int(input("How old are you ? "))
if ann > 20 :
    print("Guess your legally legal \n welcome ")#the indent removed means if they meet the criteria  the loop will break and this statement is executed

##using the not logical operator with a while loop to create a way to break out of the loop
sport = input("What sport doyou like to play?  (q to quit) : ")
while not sport == "q" :#make sure the q is in quotes to notify python a string q is the one it should watch out for
    print(f"You play  {sport}..... nice...")
    sport = input("What  other sport do you like to play? (press q to quit) : ")
    #her we can exit the loop and make  a print statement for when th user presses q
print("Okay bye.....")


##Working with lists
#####They can contain any data types together lol
r = [7,2,'love',9.6,True]
g = [9,"creepin",2,5]
u = r + g
print(u) #joins both of them into a single string

#we can also use some python inbuilt functions
                        ##indexing starts from 0 .....positive indexing ignores the upper limit but negative indexing includes the upper limit as well
#3list slicing  -  just getting a portion of the list
#same principles for lists work on strings as well
print(r[3])
print(r[:4])
print(r[-4:])
#another way to index the last item in a list or string we either use the -1 or a numberabove the index of the last item
print(g[-1])
print(g[1])
print(g [::2]) #to skip 2 spaces 
print(g[1::2]) #start from index 1 then skip 2 values



p = [2,3,65,8,9,63]
d = ["opio",2,87,5,3,65]
w = p + d
r = set(w)
p.append("joana")#we donont eqaute this statement to anything ##this adds at the end
print(p)
print(w)#lists allow duplicates 
print(r)#donot allow duplicates

##insert adds at a n index holder
d.insert(3,"library")##this gets the exact index you wanna replace with and fills the item into that exact index``
print(d)

##we can remove something from the list
d.remove("opio")
print(d)

#we can remove at a specific index 
p.pop(4)
print(p)

##lists are mutable ... we  can change their contents
p[1]=200
print(p)



#######    () - tuples
#######    [] - lists
#######    {} - sets and dictionaries




###creating dictionaries
dict1 = {
    "ricta" : 4, "keks" : 8, "Jameson" : 10
}

dict2 = {
    "names" :dict1
}

print(dict2)
#calling out a single value from a dictionary
##we use the [] to go from one key to another till we 
print(dict2["names"]["Jameson"])

##only in dictionaries can we change values...but not keys
##if it runs and doesnt find a key you told it to find it creates it and gives it values
dict2["classes"]=(9,4,5)
print(dict2)##it created the classes key

dict2["classes"] = (2,3,65)
print(dict2)


###File handling
r = read
w = write
x = create
a = append
r+ = read and write

file = open("gay.py","x") #this file is created in the directorycontaing this pytyhon script...

file = open("les.py", "w")#This file isnt  there so python will create it then write to it
file.write("Today is a good day")#3this will write to the fileyouve just created
file.close()#This closes your file from being edited any more
##since the file is closed we donot just write to itagain.. this tells python to erase allthe data andwrite afresh in the file... so we append if we wannaadd data t the file
file = open("les.py","a")
file.write(" iam sold out")
file = open("les.py","r")
print(file.read())

###ooooorrrrrrrr
#we use the with open function which automatically closes the file for you
adds = "My name is Kawooma Elijah\nAnd iam officially a real nigga\n From today on, i nolonger have lugambo or lumamonga cause iam a focused nigga init "
with open("keks.txt","w") as file:
    file.write(f"\nThis file contains text and test text like {adds}")
with open("keks.txt",'r')as file:
    print(file.read())
with open("Bro.txt","w") as file:
    file.write("Iam a straight as Ugandan male init")   
'''

















