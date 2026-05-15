
# 1. Different Types of Inheritance in Python
# Single Inheritance
class Parent:
    def show(self):
        print("Parent class")

class Child(Parent):
    def display(self):
        print("Child class")

obj = Child()
obj.show()
obj.display()

# Multilevel Inheritance
class GrandParent:
    def gp(self):
        print("Grand Parent")
class Parent1(GrandParent):
    def p(self):
        print("Parent")
class Child1(Parent1):
    def c(self):
        print("Child")
obj = Child1()
obj.gp()
obj.p()
obj.c()

# Multiple Inheritance
class Father:
    def father_method(self):
        print("Father class")

class Mother:
    def mother_method(self):
        print("Mother class")

class Son(Father, Mother):
    pass

obj = Son()
obj.father_method()
obj.mother_method()

# Hierarchical Inheritance
class Parent2:
    def parent(self):
        print("Parent class")
class ChildA(Parent2):
    pass

class ChildB(Parent2):
    pass
a = ChildA()
b = ChildB()
a.parent()
b.parent()

# 2. Employee Class with work() and getSalary()

class Employee:
    def work(self):
        print("Employee is working")

    def getSalary(self):
        print("Salary is 50000")

emp = Employee()
emp.work()
emp.getSalary()


# 3. HRManager Subclass

class Employee:
    def work(self):
        print("Employee is working")

class HRManager(Employee):
    def work(self):
        print("HR Manager manages employees")

    def addEmployee(self):
        print("New employee added")

hr = HRManager()
hr.work()
hr.addEmployee()


# 4. Program to Show Polymorphism

class Bird:
    def sound(self):
        print("Bird makes sound")

class Dog:
    def sound(self):
        print("Dog barks")

for obj in (Bird(), Dog()):
    obj.sound()


# 5. Program to Show Method Overloading

class Addition:
    def add(self, a, b, c=0):
        print("Sum =", a + b + c)

obj = Addition()

obj.add(10, 20)
obj.add(10, 20, 30)


# 6. Program to Show Method Overriding

class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        print("Child method")

obj = Child()
obj.show()


# 7. Person Class

class Person:
    def getFirstName(self):
        return "John"

    def getLastName(self):
        return "Doe"

p = Person()

print(p.getFirstName())
print(p.getLastName())


# 8. Employee Subclass with Employee ID

class Person:
    def getFirstName(self):
        return "John"

    def getLastName(self):
        return "Doe"

class Employee(Person):
    def getEmployeeId(self):
        return 101

    def getLastName(self):
        return "Doe - Manager"

emp = Employee()

print(emp.getFirstName())
print(emp.getLastName())
print(emp.getEmployeeId())



# 11. Employee Hierarchy Program

class Employee:
    def __init__(self, name, address, salary, job_title):
        self.name = name
        self.address = address
        self.salary = salary
        self.job_title = job_title

    def calculate_bonus(self):
        return self.salary * 0.10

    def performance_report(self):
        print(self.name, "has good performance")

    def manage_project(self):
        print(self.name, "is managing projects")


class Manager(Employee):
    pass


class Developer(Employee):
    pass


class Programmer(Employee):
    pass


m = Manager("Ravi", "Hyderabad", 80000, "Manager")

print("Bonus:", m.calculate_bonus())

m.performance_report()

m.manage_project()


# 12. Program to Explain Dynamic Binding

class Animal:
    def sound(self):
        print("Animal sound")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

obj = Cat()
obj.sound()


# 13. Program to Show super() Keyword

class Parent:
    def show(self):
        print("Parent class")

class Child(Parent):
    def show(self):
        super().show()
        print("Child class")

obj = Child()
obj.show()


# # 14. Program to Show this Keyword (self in Python)

# class Student:
#     def __init__(self, name):
#         self.name = name

#     def display(self):
#         print("Name:", self.name)

# s = Student("Dora")
# s.display()


# 15. Program to Show static Keyword--python doesnot support static keyword but In Python, variables defined directly inside a class body (and outside any methods) are called class variables. 

class College:
    college_name = "KIET"

    def display(self):
        print("College Name:", College.college_name)

obj1 = College()
obj2 = College()

obj1.display()
obj2.display()


# 16. Program to Show Access Modifiers

class Demo:
    public_var = "Public"

    _protected_var = "Protected"

    __private_var = "Private"

obj = Demo()

print(obj.public_var)

print(obj._protected_var)

# Private variable access
print(obj._Demo__private_var)