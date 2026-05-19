class parent:
    def show(self):
        print("parent class")
class child(parent):
    def display(self):
        print("child class")
s=child()
s.show()
s.display()
## =multilevel inheritance
class a:
    def show(self):
        print("class a")
class b(a):
    def showb(self):
        print("class b")
class c(b):
    def showc(self):
        print("class c")
s=c()
s.show()
s.showb()
s.showc()
##multiple inheritance
class a:
    def add(self):
        print("geetha")
class b:
    def subtract(self):
        print("deepu")
class c(a,b):
    def multi(self):
        print("who is these")
d=c()
d.add()
d.subtract()
d.multi()
##huierarchical
class hie:
    def dis(self):
        print("parent from extends")
class child1(hie):
    def display(self):
        print("child1 is fast")
class child2(hie):
    def display(self):
        print("child2 is slow")
c1=child1()
c1.display()
c1.dis()
c2=child2()
c2.display()
c2.dis()
##employess salriews
class Employee:
        def work(self):
            print("employee is working")
        def getSalary(self):
            print("employtee salary is 34000")
S=Employee()
S.work()
S.getSalary()
##HR MANAGER SUB CLASS
class Employee:
    def work(self):
        print("employee is working")
class hrmanager(Employee):
    def work(self):
        print("hr is working bro")
    def addemployee(self):
        print("new employee is added")
s=hrmanager()
s.work()
s.addemployee()
##polymorphism 
class Employee:
    def miracle(self):
        print("miracle is a good company")
class e2(Employee):
    def miracle(self):
        print("miracle has nice management")
class e3(Employee):
    def miracle(self):
        print("miracle is a good place to work")
r=e3()
r.miracle()
r1=e2()
r1.miracle()
r2=Employee()
r2.miracle()
##overloading means same class with different parameters
class addition:
    def add(self,a,b,c):
        print(a+b+c)
r=addition()
r.add(10,0,88)
r.add(1,2,3)
#method overriding means same method name in parent and child but the parameters changes in child class
##person names geeting his first name and last name
class person:
    def getfirstname(self):
        print("geetha")
    def getlastname(self):
        print("gangabattula")
d=person()
d.getfirstname()
d.getlastname()
""" Create a subclass called Employee that adds a new method named
getEmployeeId() and overrides the getLastName() method to include the
employee's job title."""
class person:
    def getlastname(self):
        print("gangabattula")
class e2(person):
    def getlastname(self):
        print("gangabattula is a software trainee at miracle")
    def getemployeeid(self):
        print(6504)
t=e2()
t.getlastname()
t.getemployeeid()
##abstracxtion means hiding the internal details and showing only the functionality to the user
from abc import ABC,  abstractmethod
class college(ABC):
    @abstractmethod
    def which(self):
        pass
class first(college):
    def which(Self):
        print("im from kiet college")
class second(college):
    def which(self):
        print("im from gits college")
c1=first()
c1.which()
c2=second()
c2.which()
##interface means a class with only abstract methods
from abc import ABC, abstractmethod
class animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class eagle(animal):
    def sound(self):
        print("eagle makes sound like screech")
class fox(animal):
    def sound(self):
        print("fox makes sound like bark")
e=eagle()
e.sound()
f=fox()
f.sound()
##i creating an big calcula
"""11. Write a Java program that creates a class hierarchy for employees of a
company. The base class should be Employee, with subclasses Manager,
Developer, and Programmer. Each subclass should have properties such as
name, address, salary, and job title.Implement methods for calculating
bonuses, generating performance reports, and managing projects."""
class employee:
    def __init__(self,name,address,salary,jobtitle):
        self.name=name
        self.address=address
        self.salary=salary
        self.jobtitle=jobtitle
    def calculatebonus(self):
        print(self.salary*0.10)
    def performance_report(self):
        print(self.name + " -> " + self.jobtitle)
class manager(employee):
    def manageproject(self):
        print("manager is managing the project")
class developer(employee):
    def developerreport(self):
        print("developer is developing the project")
class programmer(employee):
    def programmerreport(self):
        print("programmer is programming the project")
n=employee("geetha","yanam",55000,"software trainee")
n.calculatebonus()
n.performance_report()
##dynamic binding is also called late binding means the method to be called is determined at runtime
class book:
    def store(self):
        print("geethas store")
class book1(book):
    def store(self):
        print("mines store not geethas")
class book2(book):
    def store(self):
        print("balus store not geethas")
b=book1()
b.store()
b2=book2()
b2.store()
##super keyword is used for the use to share the properities and methods of parent class to chils class
class parent:
    def p1(self):
        print("parentclass")
class child(parent):
    def c1(self):
        super().p1()
        print("child class")
c=child()
c.c1()
#self keyword 
class c1:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)
s=c1("varshu")
s.display()
##STATIC keyword
class student:
    college="kiet"
    def __init__(self,name):
        self.name=name
c=student("geetha")
print(c.name)
print(c.college)
##acess modifiers
class Employee:

    def __init__(self):

        self.name = "Geetha"      # Public
        self._salary = 50000      # Protected
        self.__pin = 1234         # Private


    def private_data(self):

        print("Private PIN:", self.__pin)


e = Employee()


# Public Variable
print("Public:", e.name)


# Protected Variable
print("Protected:", e._salary)


# Private Variable Access using Method
e.private_data()


# Direct Private Access
# print(e.__pin)   ❌ Error