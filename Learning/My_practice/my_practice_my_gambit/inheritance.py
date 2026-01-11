##creating a class that borrows functionality from its parent class 

class People:
    can_talk = True #initially everyone can talk 

    def __init__(self,name):
        if not name:
            raise ValueError("You havent entered a name") ##error checking for missing name 
        self.name = name
   
    @classmethod
    def talk(cls):
        print(f"Everyone is born with the ability to talk either in their mind or with their mouth: {cls.can_talk}")


class Student(People):

    can_talk = False

    def __init__(self,name,house):
        super().__init__(name)
        self.house = house
    
    @classmethod
    def talk(cls):
        print(f"Everyone is born with the ability to talk either in their mind or with their mouth: {cls.can_talk}")

class Professor(People):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject

def main():

    person = People("Basoga") #creating a people parent instance
    student = Student("Harry","Lingoo")#this is a child of the people class and so is prof
    prof = Professor("Mr.Kiplangat","Maths")

    People.talk()#talk is a class method hence its use on a class directly 

    print(person.name)
    print(student.name)
    print(prof.name)

    Student.talk()
if __name__ == "__main__":
    main()

































