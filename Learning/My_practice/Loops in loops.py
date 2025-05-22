
##printing letters(Creating a loop in a loop)
#We first initialise a 4 loop
size = 5 

#Triangle
for i in range(size):
    for j in range(i +1):
        print("*", end ="")#end means the code will end the line with an empty space before looping
    print()
'''
#Rectangle
size = 5
for i in range(size):
    for j in range(size):
        print("*", end ="")
    print()
'''