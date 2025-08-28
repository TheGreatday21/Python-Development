#these are the conditional opertors 
# > - Greater than
# >= - Greater than or equal to 
# < - less than
# <= - less than or equal to 
# == - is equal to 
# != - not equal to  

#we use loops mostly with conditionals


def main():
    x = int(input("What's x? "))
    y = int(input("What's y? "))

    if x < y:
        print(f"{x} is less than {y}")
    elif x > y:
        print(f"{x} is greater than {y}")
    else:
        print(f"{x} is equal to {y}")



    #we can also use the logic to determine if it equal or not using the or conditional
    if x < y or x > y:
        print(f"{x} is not equal to {y}")
    else:
        print(f"{x} is equal to {y}")

        #we can also use the logic to determine if it equal or not using the or conditional
    if x != y:
        print(f"{x} is not equal to {y}")
    else:
        print(f"{x} is equal to {y}")
    
    
main()





















