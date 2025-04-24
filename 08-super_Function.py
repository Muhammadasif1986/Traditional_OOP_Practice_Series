class Person:
      def __init__(self,name):
            self.name = name

class Teacher(Person):
      def __init__(self,name,subject):
            super().__init__(name)
            self.subject = subject

      def display(self):
            print("Name: {} and Subject: {}".format(self.name,self.subject))

p1 = Person("Muhammad")

t1 = Teacher("Asif","Python")

t1.display()

print(p1.name)

