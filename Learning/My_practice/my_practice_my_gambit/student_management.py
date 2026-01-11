##A list of dictionaries containing student details 
student_list = [
    {"student_id":1,"name":"Kapeka","age":23,"course":"Bcom"}
] 

##function to handle addition of new students 
def add_student(student_list,student_id,name,age,course):
    for student in student_list:
        if student_id != student['student_id']:
            student_list.append({
                'student_id' : student_id,
                'name': name, 
                'age':age, 
                'course': course
                })

            print("Student successfully registered .... WELCOME \n")
           
        else:
             print("This student already exists in the school databases")
            
def find_student_by_id(student_list,student_id):
    for student in student_list:
        if student_id == student['student_id']:
            print(f"student name : {student['name']}, student age :{student['age']}, student course : {student['course']} ",sep= "   ")

def main():
    

    student1 = add_student(student_list,2,"Kalyango",23,"LLB")
        
    print(student_list)

if __name__ == "__main__":
    main()












































































