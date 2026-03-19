from models import *

p = Person("Alex", 30, "Almaty")
s = Student("Dana", 19, "Astana", "KBTU")
t = Teacher("John", 45, "Shymkent", "Math")

people = [p, s, t]

for person in people:
    print(person)
    print(person.get_name())
    print(person.get_age())
    print()
