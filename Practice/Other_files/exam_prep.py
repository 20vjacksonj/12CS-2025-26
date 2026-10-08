class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}")

class Teacher(Person):
    def __init__(self, subject):
        self.subject = subject

    def greet(self):
        print(f"I teach {self.subject}")

class Student(Person):
    def __init__(self, grades):
        self.grades = self.average

    def average_grade(self):
        for grade in self.grades:
            self.average += grade
        self.average = self.average / len(self.grades)


teacher = Teacher("Mr. Smith", 40, "Math")
    
student = Student("Alice", 16, [85, 90, 78])

student.greet()
teacher.greet()
print(student.average_grade())