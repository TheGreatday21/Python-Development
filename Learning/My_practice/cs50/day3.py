#loops in python are the same as in c

name = input("name: ")
t = name.capitalize() #this method is going to capitalise only the first char in the string 
z = name.upper()
l = name.lower()

print(f"name : {name}")
print(f"name : {t}")
print(f"name : {z}")
print(f"name : {l}")


                        ###  FOR LOOPS 

array = [2,1,3,4,5,6]

for i in array:
    print(i)

# we can use a function in python called range that hands you out one value at a time . Creates the number of iterations you can use 
for i in range(3):
    print("meow")


                ### WHILE LOOPS 
i = 0
while i < 3:
    print("meow ")
    i += 1




##FUNCTIONS 
#python does not really have a main function but if we are defining our own function we define it at the top of the file  and we need to call the function at the very bottom of the file 
def main():
    meow()

def meow():
    for i in range(7):#hard coding the 7 is not advised 
        print("God loves me")
print(meow())


##the  actual proper way to callmain in python is 
if __name__ == "__main__":
    main()
#mainly used when making your own libraries 




































