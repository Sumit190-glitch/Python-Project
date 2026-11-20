class Teacher:
    location = "Pandharpur"
    def  __init__(self,name):
        self.name = name
    def speak(self):
        print("Shut Uppp....")

class Student(Teacher):
    def speak(self):
        super().speak()
        print("Laughing..🤣")

d = Student("AMAN")
d.speak()
print(d.location)
print(d.name)


