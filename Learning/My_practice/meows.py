MEOWS = 3 #creating a constant variable that will not change . No specific syntax in python but convention is to make the variable capital 

for _ in range(MEOWS):
    print("meow")

######################################### OOP IMPLEMENTATION
class Cat:
    MEOWS = 3 #creating a cls variable 

    def meow(self):
        print("\n")
        for _ in range(Cat.MEOWS):
            print("meow")

cat = Cat()

cat.meow()















