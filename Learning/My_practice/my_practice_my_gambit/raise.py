##creating a class and raising my own errors lol 
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

        if not name:
            raise ValueError("The name is missing ")
        if age not in range(20,31):
            raise ValueError("Your are not in the allocated student age bracket")
       
def main():

    student = getStudent()
    print(f"{student.name} is {student.age} years old")



def getStudent():
    try:
        name = input("Name")
        age = int(input("Age"))
    except ValueError or TypeError:
        print("Ensure the right data types are used")

    return Student(name,age)


if __name__ == "__main__":
    main()











    