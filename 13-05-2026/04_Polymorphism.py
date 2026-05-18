# Program to show polymorphism in class

class Employee:
    def __init__(self, name, hours):
        self.name = name
        self.hours = hours

    def work(self):
     return f"{self.name} works for {self.hours} hours"


class Manager(Employee):
    def work(self):
        return f"{self.name} plans and manages for {self.hours} hours"


class Developer(Employee):
    def work(self):
        return f"{self.name} writes code for {self.hours} hours"


people = [
    Manager("Alice", 8),
    Developer("Bob", 7),
    Employee("Charlie", 6),
]

for person in people:
    print(person.work())