class Person:
    def show_role(self):
        print("Person: general role")


class Teacher(Person):
    def show_role(self):
        print("Teacher: teaches students")

person = Teacher()
person.show_role()
