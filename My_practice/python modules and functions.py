''''
###Handling text in pythom
# r - read
# w is write
# r+ is read and write
# x is create
# a is append
## we use the with open statement
text = "Hellooooo\n My name is Kaizzi Elijah the great bashi\n Wasap my niggas \n"
with open("keks.txt",'w') as file:
    file.write(text)
    #we have successfully created the text file called keks
# to append to it
text = "Damn what a loveley day"
with open("keks.txt",'a') as file:
    file.write(text)


##note
###incase your file is on the desktop you have to usee \\ when stating its file path .. this is the escape sequence 

#example 1
with open("keks.txt","r") as file:
    print(file.read())

##getting the file from a desktop we only use  a forward slash
with open("/Users/keksmacbookair/Desktop/keks2love.docx","r") as file:
    print(file.read())



##use of a for loop with a range  -- making the code delay while executing using time module
import time
for i in range(1,11,2):#this will print odd numbers because we told the code to skip two numbers per number
    time.sleep(1)
    print(i)

'''

####The time module
import time
print(time.ctime(0))#prints the time the computerss epach was first on
#epach is when your computer thinks time begun
##printing  time in seconds computer has been on  till current time
print(time.time())


##getting the current date and time
print(time.ctime(time.time()))
##another way 
time_object = time.localtime()
print(time_object)##to make this more understandable we use the time strftime



