Man = 88
Ars = 86

print("Use text such as Win,Draw and Loss\n")
M = input("How did the Manchester City do ? ")
A = input("How did Arsenal do ?")

if M == "Win" :
    Man += 3
elif M == "Draw":
    Man += 1
elif M == "Loss":
    Man += 0
if A =="Win":
    Ars += 3
elif A == "Draw":
    Ars += 1
elif A == "Loss":
    Ars += 0
    
if Man > Ars :
    print("Mancity will be crowned champions")
elif Ars > Man :
    print("Arsenal will be crowned champions")
else:
    print("Its a tie , the winner will be decided by goal difference")








    








