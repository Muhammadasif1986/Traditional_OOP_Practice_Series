class Student:
      """
      1. Using self
Assignment:
Create a class Student with attributes name and marks. Use the self keyword \
to initialize these values via a constructor. Add a method display() that \
prints student details.
      """
      def __init__(self,name,marks):
            self.name = name
            self.marks = marks

      def display(self):

            print(f"Student Name is: {self.name} and Student Marks is: {self.marks}")

student = Student("Muhammad Asif", 350)
print(Student.__doc__)
student.display()



