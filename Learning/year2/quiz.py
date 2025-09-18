

class Car:
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color 
    def drive(self):
         vreturn f"Iam driving a {self.color} {self.make} {self.model} car from the year {self.year} "

def main():

    #creating the first instance of our class Car
    car1 = Car("Toyota","Supra",2013,"Green")

    #changing some of the attribute values in my object
    car1.color = "Red"
    car1.year = 2023

    print(car1.drive())


if __name__ == "__main__":
    main()