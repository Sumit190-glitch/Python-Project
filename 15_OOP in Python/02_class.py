class  Employee:
    
    def __init__(self, salary, name, assigned):
        self.salary = salary
        self.name = name
        self.assigned = assigned

    def get_info(self):
        print(f"Employee is {self.name},He is bonded for {self.assigned} years and his getting {self.salary} per anum for that.")

e = Employee(500000, "Prashant kelkar", 2)
e.get_info()


