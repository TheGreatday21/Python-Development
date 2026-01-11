#use of the at classmethod 
#@classmethod - This a  class method you can call without instanciating an object . pretty cool 
##You just simply apply it directly to the class like how you would to an object

import random

class Student:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"{self.name} is of color {self.color}"

class Hat:
#class variables are those shared by every single object in the class 
    names = ['John','James','Joseph',"Harry","Tyrone"]

    @classmethod##this is a class method 
    #we change from self to cls as first argument 
    def sort(cls):
        name = random.choice(cls.names)#we randomise the things in the class variable (list)
        match name:
            case 'Harry':
                print(f"Your in gryfindor {name}") 
            case 'John':
                print(f"Your in Kabalega {name} ")
            case 'Tyrone':
                print(f"Your black {name}")
            case _ :
                print(f"Hmmm, we donot know you {name}")
         


#creating a hat object 
hat = Hat()
stud = Student("Harry","Red")
stud2 = Student("John","Green")

Hat.sort()
Hat.sort()
print(stud)


