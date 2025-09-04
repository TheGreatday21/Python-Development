#switch statements in python we use something called match 


name = input("Whats your name: ")

if name == "Harry":
    print("Gryfindoor")
elif name == "Ron":
    print("Gryfindoor")
elif name == "Hermione":
    print("Gryfindoor")
elif name == "Draco":
    print("Slytherin")
else :
    print("Whoo?")


#second way can use is  
if name == "Hermione" or name == "Harry" or name == "Ron" :
    print("Gryfindoor")
elif name == "Draco":
    print("Slytherin")
else :
    print("Whoo?")


#the third way is using the match statement also known as the switch statement in c c++ and javascript

match name:
    case "Harry":
        print("Gryfindoor")
    case "Hermione":
        print("Gryfindoor")
    case "Ron":
        print("Gryfindoor")
    case "Draco":
        print("Slytherin")
    case _:    #this is the syntax for the rest of cases not addressed in the match statement
        print("Who..?")


#the other way is to use or but in this case its | 
match name:
    case "Harry" | "Harry" | "Ron":
        print("Gryfindoor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who..?")