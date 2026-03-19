class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        return f"My name is {self.name}. I am {self.age} years old."

    def work(self):
        return f"{self.name} is doing some work."

    def __str__(self):
        return f"Person(name={self.name}, age={self.age}, city={self.city})"


class Student(Person):
    def __init__(self, name, age, city, university):
        super().__init__(name, age, city)
        self.university = university

    def work(self):
        return f"{self.name} is studying at {self.university}."

    def attend_class(self):
        return f"{self.name} is attending a class."

    def __str__(self):
        return f"Student(name={self.name}, age={self.age}, city={self.city}, university={self.university})"


class Teacher(Person):
    def __init__(self, name, age, city, subject):
        super().__init__(name, age, city)
        self.subject = subject

    def work(self):
        return f"{self.name} is teaching {self.subject}."

    def check_homework(self):
        return f"{self.name} is checking homework."

    def __str__(self):
        return f"Teacher(name={self.name}, age={self.age}, city={self.city}, subject={self.subject})"