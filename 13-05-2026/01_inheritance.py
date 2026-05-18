# single Level Inheritance

class Parent:
    def height(self):
        return "Iam 6 feet Tall"
    
class Child(Parent):
    def height(self):
        parent_height = super().height()
        return f"My parent is {parent_height} but Iam 5 feet Tall"

c = Child()
print(c.height())


# Multi Level Inheritance. 

class GrandParent:
    def property(self):
        acres = 15
        return f"{acres} acres of land"

class Parent(GrandParent):
    def house(self):
        return "I have a big house"

class Child(Parent):
    def car(self):
        return "I have a car"

c = Child()
print(c.property(),"\n",c.house(),"\n",c.car())


# Multiple Inheritance

class Samsung:
    def software(self):
        return "Android"

class Iphone:
    def camera(self):
        return "128MP"

class OnePlus:
    def display(self):
        return "green line"

class Mobile(Samsung, Iphone, OnePlus):
    def Universe(self):
        return "I have an Ai assisted universe"

m = Mobile()
print(m.software(),"\n",m.camera(),"\n",m.display(),"\n",m.Universe())


# Hierarchical Inheritance

class Employee:

    def __init__(self, name, id):
        self.name = name
        self.id = id
    
class Manager(Employee):
    def manage(self):
        return f"{self.name} is managing the team with id {self.id}"

class Developer(Employee):
    def develop(self):
        return f"{self.name} is developing the software with id {self.id}"

class Programmer(Employee):
    def program(self):
        return f"{self.name} is programming the code with id {self.id}"

m1 = Manager("Alice", 101)
print(m1.manage())
m2 = Developer("Bob", 102)
print(m2.develop())
m3 = Programmer("Charlie", 103)
print(m3.program())

