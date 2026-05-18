class Employee:
    def __init__(self,hours):
        self.hours = hours

    def work(self):
        return self.hours
    def getSalary(self):
        return self.hours * 1000

class HRManager(Employee):
    def work(self):
        return f"HR Manager is working for {self.hours} hours"

e = Employee(8)
h = HRManager(7)
print(h.work())
print(h.getSalary())
print(e.work())
print(e.getSalary())


