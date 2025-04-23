class Employee:
      def __init__(self,name,salary,ssn):
            self.name = name
            self._salary = salary
            self.__ssn = ssn

      def get__ssn(self):
            return self.__ssn

emp = Employee("asif",50000 , "123-23-44")

print(emp.name)
print(emp._salary)
print(emp.get__ssn())
print(emp._Employee__ssn)