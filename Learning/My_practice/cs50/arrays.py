#arrays in python are linked lists 

#some functions include :
# 1. len 

scores = [72,73,33]
average = sum(scores) / len(scores)

print(f"average is  : {average}")

# getting the scores from the users 

grades = []

for i in range(4):
    grade = int(input("Score : "))
    grades.append(grade)


average2 = sum(grades) / len(grades)

print(f"average is : {average2}")