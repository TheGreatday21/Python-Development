class StudentResult :
  def __init__(self,student_name,course,marks):
    self.student_name = student_name
    self.course = course
    self.marks = marks
    
  def calculate_grade(self):
    if self.marks >= 80:
      return f"Name: {self.student_name} \nCourse:{self.course}\nGrade: A\n "
    elif self.marks >= 70:
      return f"Name: {self.student_name} \nCourse:{self.course}\nGrade: B\n "
    elif self.marks >= 60:
      return f"Name: {self.student_name} \nCourse:{self.course}\nGrade: C\n "
    elif self.marks >= 50:
      return f"Name: {self.student_name} \nCourse:{self.course}\nGrade: D\n "
    else:
      return f"Name: {self.student_name} \nCourse:{self.course}\nGrade: F\n "

def main():
  #instance of the book class
  student1 = StudentResult("Elijah", "BSDS", 88)
  student2 = StudentResult("James","BSCS",94)
  student3 = StudentResult("Lipo","BVAD",63)
  
  
  
  print(student2.calculate_grade())
  #output is Grade A
  
  print(student1.calculate_grade())
  #output is Grade A
  
  print(student3.calculate_grade())
  #prints Grade C
  #updating mark to see if grade changes 
  student3.marks = 54
  print(student3.calculate_grade())
  #updating mark changes Grade to D
  
   
if __name__ == "__main__":
    main()