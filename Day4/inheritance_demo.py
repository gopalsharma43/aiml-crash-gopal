# This program demonstrates inheritance in Python.

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."


class Student(Person):

    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def study(self):
        return f"{self.name} is studying."


class Teacher(Person):

    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        return f"{self.name} teaches {self.subject}."


student = Student("Gopal", 20, 101)
teacher = Teacher("Sharma Sir", 35, "Python")

print(student.introduce())
print(student.study())

print()

print(teacher.introduce())
print(teacher.teach())