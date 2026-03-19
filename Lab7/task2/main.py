from models import Person, Student, Teacher


def main():
    p1 = Person("Mansur", 30, "Almaty")
    s1 = Student("Dana", 19, "Astana", "KBTU")
    t1 = Teacher("Osman", 45, "Shymkent", "Mathematics")

    people = [p1, s1, t1]

    for person in people:
        print(person)
        print(person.introduce())
        print(person.work())
        print()


if __name__ == "__main__":
    main()