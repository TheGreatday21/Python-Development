#this code will illustrate the use of enums  in python
from enum import Enum
#creating a class that inherits from enum
#Enum is used with a fixed set of options e.g a lamp only has an on and off state
class Color(Enum):
    RED  = 'R'
    GREEN  = 'G'
    BLACK  = 'B'
'''  
print(Color('R'))
print(Color.RED)
print(repr(Color.RED))
print(Color.RED.name)
print(Color.RED.value)
'''
def create_car(color:Color) -> None:
    match color:
        case Color.RED:
            print(f"A smoking red hot car was created\n")
        case Color.GREEN:
            print(f"A sexy lime green car was created\n")
        case Color.BLACK:
            print(f"A matt blackcar was created\n")
        case _:
            print(f"We donot have the color {color} in our data base\n")
create_car(Color.GREEN)






