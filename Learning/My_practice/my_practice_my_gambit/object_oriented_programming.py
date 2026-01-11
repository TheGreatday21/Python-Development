
import sys

#creating a class car to have car objeects 
class Car:
    #creating a constructor to have object attributes
    def __init__(self,name,year,nin,model,color):
        self.name = name    
        self.year = year
        self.model = model
        self.color = color
        self.__nin = nin #this is a protected attribute 

    ##creating a few methods to give this car functionality of-a-sort
    def drive(self):
        print(f"Your car ,the {self.name} can drive only 400km on a full tank ")

    def about_car(self):
        print(f"Your car is a {self.year} {self.model} {self.name} that is {self.color} in color ")

    ##creating a getter and a setter to modify the protected attribute 
    @property#this creates a getter 
    def nin (self):
        return f"Your cars nin is {self.__nin}"

    @nin.setter
    def nin(self,input):
        #error checking so that the nin is not messed up 
        try:  
            if type(input) is not int:  
                sys.exit("The nin should be an integer with  10 values")
        except Exception:
            print("the nin must be a set of 10 positive  integers ")

        else:  
            str_input = str(input)
            if len(str_input) == 10:
                print(f"You have changed the nin number of {self.name} to {input}")
            else:
                print("The nin has to be  10  values")

def main():
    #creating a car instance 

    car1 = Car("Forrester",2021,12345677890,"Subaru","Red")

    car1.about_car()
    car1.drive()
    print(car1.color) #normal attributes can easily be accessed and changed 
    car1.color = "Black"
    print(car1.color)#color changed to black now 

    #testing the getter and setter for the private attribute 
    print(car1.nin)###GETTER

    #car1.nin = 0000000009 #returns an error for leading zeros error 
    car1.nin = 1000000000

if __name__ == "__main__":
    main()