
A = int(input("What score did you get in Math"))
B = int(input("What score did you get in Writing skills"))
C = int(input("What score did you get in Structured programming"))
D = int(input("What score did you get in Essentials of Softwware"))
E = int(input("What score did you get in Data science"))
count = 0

if  A > 50:
    count += 1
else:
    count += 0
if  B > 50:
    count += 1
else:
    count += 0
if  C > 50:
    count += 1
else:
    count += 0

if  D > 50:
    count += 1
else:
    count += 0

if  E > 50:
    count += 1
else:
    count += 0

print(f"Your total count score is {count}")
if count == 5:
    print("Pass")
else:
    print("Fail")







