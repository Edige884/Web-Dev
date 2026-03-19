class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def __str__(self):
        return f"{self.name}, {self.age}, {self.city}"


class Student(Person):
    def __init__(self, name, age, city, university):
        super().__init__(name, age, city)
        self.university = university

    def get_university(self):
        return self.university

    def __str__(self):
        return f"Student(name={self.name}, age={self.age}, city={self.city}, university={self.university})"


class Teacher(Person):
    def __init__(self, name, age, city, subject):
        super().__init__(name, age, city)
        self.subject = subject

    def get_subject(self):
        return self.subject

    def __str__(self):
        return f"Teacher(name={self.name}, age={self.age}, city={self.city}, subject={self.subject})"