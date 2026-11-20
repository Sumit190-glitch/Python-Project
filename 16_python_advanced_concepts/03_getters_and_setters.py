class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = str(salary)
    
    @property
    def first_name(self):
        s = self.name.split(" ")
        return s[0]
    
    @first_name.setter 
    def first_name(self, first):
        s = self.name.split(" ")
        new_name = f"{first} {s[1]}"
        self.name = new_name

y = Employee("Dhairyashil Pawar", 20000000)
# print(y.first_name())
# y.set_first_name("Sushant Dhairyashil")
# print(y.name)

print(y.first_name)
y.first_name = "Sushant"
print(y.name)
