# we are iterating over strings 

students = ["Elijah", "James", "John"]#this is a list of strings 

for student in students: 
    print(student) #the student variable automatically tracks the values at the respective indexes of the list 


#another way is to use the length function 
for i in range(len(students)):
    print(students[i])