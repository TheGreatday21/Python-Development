"""
Task is to design a class based system for a city adventure game where players control characters and 
vehicles to complete missions in an open world environment The solution should focus on using object orientted programming princupltles 
to create fundamental game elements 
"""

class Character:
    def __init__(self,name,health,position):
        self.__name = name
        self.__health = health
        self.__postion = position

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,input):
        self.__name = input
        print("Changed the name of character")

    @property
    def health(self):
        return self.__health
    @health.setter
    def health(self,input):
        self.__health = input
        print("Health has been updated")

    @property
    def position(self):
        return self.__postion
    @position.setter
    def position(self,input):
        self.__position = input
        print("Position has been updated")

    def move(self):
        print(f"{self.__name} is moving from {self.__postion}")

    def attack(self,thing):
        print(f"{self.__name} is attacking the {thing}")

    def interact(self,instance) ->str: #this allows to characters to interact with each other 
        return f"{self.__name} is interacting with {instance.name} "


    def get_in(self,car):
        print(f"{self.__name} is now entering the {car.v_type}")

    def get_out(self,car):
        if car.drive:
            car.refuel = "Mid"
            print(f"{car.refuel} fuel level left")

        print(f"{self.__name} is now getting out of the {car.v_type}")


class Vehicle:
    def __init__(self,v_type,speed,fuel_level):
        self.__v_type = v_type
        self.__speed = speed
        self.__fuel_level = fuel_level

    @property
    def v_type(self):
        return self.__v_type
    @v_type.setter
    def v_type(self,input):
        self.__v_type = input
        print("You have successfully changed the type of car you are using")
    

    def drive(self,instance):
        return f"{instance.name} drove the {self.__v_type} to {instance.position}"
   
    
    @property#made the refuel to a getter and created a setter for the fuel level as well
    def refuel(self):
      return self.__fuel_level

    @refuel.setter
    def refuel(self,input):
        self.__fuel_level = input
        print(f"Fuel level updated")

    def stop(self):
        ...


def main():
#creating character instances
    character1 = Character("The Rock",100,"Birmingham")
    character2 = Character("Kevin",100,"East-London")
#creating vehicle instances
    veh1 = Vehicle("Cardilac Escallade",340,"Full")
    veh2 = Vehicle("Ford GT Mustang",320,"Full")

#instances interactions
    character1.move()
    character2.move()

    character1.attack("Dragon")
    character2.attack("Lion")

    print(character1.interact(character2))

    
    character1.get_in(veh1)
    veh1.drive(character1)
    character1.get_out(veh1)
    


if __name__ == "__main__":
    main()

































































