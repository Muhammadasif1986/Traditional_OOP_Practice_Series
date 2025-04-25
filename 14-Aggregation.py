class Employee:
    """
    Aggregation ek "Has-A" relationship hai jisme ek class doosri class ka reference\
 rakhti hai, lekin donon objects independent hote hain.

💬 “Aggregation means ‘a whole’ has ‘parts’, but those parts can exist independently.”
    """
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []   # 🔹 List of aggregated employees

    def add_employee(self, emp):
        self.employees.append(emp)

    def show_employees(self):
        print(f"{self.name} Department Employees:")
        for emp in self.employees:
            print(f"- {emp.name}")

e1 = Employee("Asif")
e2 = Employee("Ahmed")

d1 = Department("Software")
d1.add_employee(e1)
d1.add_employee(e2)

d1.show_employees()

print(e1.__doc__)
                 # ✅ Employee still exists!
