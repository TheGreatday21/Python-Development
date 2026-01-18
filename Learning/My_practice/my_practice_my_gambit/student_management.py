

def add_student(student_list,student_id,name,age,course):
    for students in student_list: #each student is a dictionary
        for student in students:
            if student_id != student['student_id']:
                student_list.append({
                    'student_id':student_id,
                    'name':name,
                    'age':age,
                    'course':course
                })
            else:
                print("This student most likely already exists in our database sorry")

def main():
    student_list =  []

    add_student(student_list,1,"Jane",21,"BSDS")
    add_student(student_list,2,"Charlotte",24,"BSDS")
    add_student(student_list,3,"Simon",21,"BSCS")

    print(student_list)

if __name__ == "__main__6t ":
    main()





































