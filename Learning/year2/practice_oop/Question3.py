class Vehicle:
  def __init__(self,model,fuel_capacity,fuel_level):
    self.model = model
    self.fuel_capacity = fuel_capacity
    self.fuel_level = fuel_level
    self.max_fuel = 100
    
  def get_fuel_level(self):
    return f"car:{self.model} \nFuel level:{self.fuel_level}\n"
  
  def refuel(self,amount):
    if self.fuel_level == "Full":
      print(f"You have a {self.fuel_level}tank at {self.fuel_capacity} liters capacity")
      print("No need to refuel")
      
    elif self.fuel_level != "Full":
      if amount <= 0:
        print("Amount must be greater than 0")
      else:
        liters = amount//4300#getting the liters 
        self.fuel_capacity += liters
        if self.fuel_capacity > self.max_fuel:
          print(f"The fuel amount is to high . You only need {self.max_fuel - self.fuel_capacity} liters")
        elif self.fuel_capacity == self.max_fuel:
          self.fuel_level = "Full"
          print(f"Refilled {liters} liters for {amount} ugx.\nCar: {self.model}\nCurrent fuel level: {self.fuel_level} \n")
        elif self.fuel_capacity >= (self.max_fuel*0.5):
          self.fuel_level = "Mid"
          print(f"Refilled {liters} liters for {amount} ugx.\nCar: {self.model} \nCurrent fuel level: {self.fuel_level} \n")
        else:
           print(f"Refilled {liters} liters for {amount} ugx. \nCar: {self.model} \nCurrent fuel level: {self.fuel_level} \n")
  
  def consume(self,distance):
    if distance <= 0 :
      print("Your journey doesnt consume any fuel")
      
    else:
      litresConsumed = 0.05 * distance #assuming 1km takes 0.05 liters of fuel
      if litresConsumed > self.fuel_capacity:
        print("The journey needs to be done in bits.\nCurrrent Fuel level cannot complete it fully. \nRefueling advised \n")
      else:
        self.fuel_capacity -= litresConsumed
        if self.fuel_capacity is 100:
          self.fuel_level = "Full"
          print(f"Trip length {distance} km\nFuel Consumed: {litresConsumed} liters\nCurrent Fuel level: {self.fuel_level}\nCurrent capacity: {self.fuel_capacity} liters\n")
        elif self.fuel_capacity in range(50,70):
          self.fuel_level = "Mid"
          print(f"Trip length {distance} km\nFuel Consumed: {litresConsumed} liters\nCurrent Fuel level: {self.fuel_level}\nCurrent capacity: {self.fuel_capacity} liters\n")
        elif self.fuel_capacity in range(1,49):
          self.fuel_level = "Low"
          print(f"Trip length {distance} km\nFuel Consumed: {litresConsumed}\nCurrent Fuel level: {self.fuel_level}\nCurrent capacity: {self.fuel_capacity} liters\n")
        else: 
          self.fuel_level = "High"
          print(f"Trip length {distance} km\nFuel Consumed: {litresConsumed}\nCurrent Fuel level: {self.fuel_level}\nCurrent capacity: {self.fuel_capacity} liters\n")
      
def main():
  #instance of the book class
  ###ASSUMING THE MAXIMUM FUEL LEVEL FOR ALL THE CARS IS 100
  vehicle1 = Vehicle("Toyoto Hilux", 90, "High") 
  vehicle2 = Vehicle("Maclaren P1",100,"Full")
  vehicle3 = Vehicle("Nissan GT",50,"Mid")
  vehicle4 = Vehicle("Honda civic",10,"Low")
  
  #before a trip
  print(vehicle1.get_fuel_level())#High before trip 
  
  vehicle1.consume(460)#the distance of the trip is 800km 
  
  #after the trip
  print(vehicle1.get_fuel_level()) #now mid because its close to half capacity
  

if __name__ == "__main__":
    main()