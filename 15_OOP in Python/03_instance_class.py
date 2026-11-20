class  Employee:
     company = "LOQ"
     def __init__(self, salary, name, assigned, company):
        self.salary = salary
        self.name = name
        self.assigned = assigned
        self.company = company

     def get_info(self):
        print(f"Employee is {self.name},He is bonded for {self.assigned} years and his getting {self.salary} per anum for that.")

e = Employee(500000, "Prashant kelkar", 2, "rox" )
print(e.company)
print(Employee.company)
print(e.get_info)
print(dir(e))
