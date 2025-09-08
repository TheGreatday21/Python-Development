#switch statements are called someting else in  python. Here we use something called match 


name = input("Whats your name: ")

#the old fashioned way is to use elif and if statements 
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


#second way can use is to use if and elif statements with conditionals 
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

#####GENERALLY IN PYTHON IF WE WANT TO EITHER USE A VARIABLE WE DONOT NEED TO ADDRESS LATER IN THE LOOP WE USE _ AND IF WE WANT TO ADDRESS ALL THE REMAINNIG CASES WE HAVE NOT ADDRESSED IN THE MATCH STATEMENT WE ALSO USE THE _


#the other way is to use or but in this case its written as | 
match name:
    case "Harry" | "Harry" | "Ron":
        print("Gryfindoor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who..?")