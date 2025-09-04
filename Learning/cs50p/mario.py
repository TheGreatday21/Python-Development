#creating the mario brick walls using hashes as visuals

def main():
    '''
    for _ in range(3): #the underscore is a way to use a variable we donot need to use later in the loop
        print("#")
    '''
    length = int(input("How tall is the wall : "))
    size = int(input("How thick is the wall : "))
    printBricks(length,size)
    print_row(size)


def printBricks(height,width):
    
    for _ in range(height):

        for _ in range(width):

            print("#",end ="") 

        print("")

def print_row(width):
    print("?" * width, end="")


main()



