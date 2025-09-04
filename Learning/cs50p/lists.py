#this is a python script about lists in python 
def main():
    food = ["Rice", "Matooke","Pork","Irish"]

    for f in food:
        print(f)
    for i in range(len(food)): #Getting the number of items in the list using the len function
        #this is doing things dynamically 
        print(food[i], end="/--/") 
main()






