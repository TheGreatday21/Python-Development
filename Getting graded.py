
##Using If statemnets
#Making a proggram to return the grade of a student above 80 is A ,70 -80  is B, then C
#Using a function "def"
def grade(score) :
    if score > 80:
        return "A"
    elif score > 70:
        return "B"
    elif score >60:
        return "C"
    elif score >50:
        return "D"
    elif score >40:
        return "E"
    else :
        return "F"
a = int(input("What did you get in  math?"))
print("You got an",grade(a), "in math")
b = int(input("What did you get in chemicstry?"))
print("You got a ",grade(b),"in chemistry")































































