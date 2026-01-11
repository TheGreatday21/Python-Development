#are synatax above a function to change its functionality 

class Car:
    def __init__(self,name,year,color):
        self.name = name 
        self.year = year
        #making colour a private attribute 
        self.__color = color

    @property #this is now a getter 
    def color(self):
        return self.__color
    @color.setter
    def color(self,input):
        self.__color = input
        print(f"You have changed the color of your car to {input}")

    def car(self):
        print("A car can drive")



class Bently(Car):
    #this is a child class for the car class.
    ...


def main():
    car = Car("Ford mustang",2023,"red")
    print(car.name,car.year)
    #print(car.__color)##cannot be accessed so we use a getter and setter

    print(car.color) #using the getter
    car.color = "blue"


if __name__ == "__main__": 
    main()
