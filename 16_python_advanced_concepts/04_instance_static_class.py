class Employee:
    College = "Sveri"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    #instance method (Default)
    def print_info(self):
        info = f"The name is {self.name} and the Salary in future {self.salary}."
        print(info)
    
    #Static Methods
    @staticmethod
    def sum(a, b):
        return a+b
    
    #Class Methods
    @classmethod
    def print_College(cls):
        print(cls.College)
        

    @classmethod
    def change_College(cls, c2):
        cls.College = c2

        


e1 = Employee("Sumit", 40000)
e2 = Employee("Smit", 50000)
# print(Employee.College)
# print(Employee.name)#This will always gives an error
# print(e1.print_info)
# print(e2.print_info)
# e1.print_info()
# e2.print_info()
# print(e1.sum(22, 5))
# print(e2.sum(12, 12))
e1.print_College() #you can also write print(Employee.College)
e1.change_College("Coep")
e1.print_College() #you can also write print(Employee.College)
# print(Employee.College)
# e1.change_College("Coep")
# print(Employee.College)