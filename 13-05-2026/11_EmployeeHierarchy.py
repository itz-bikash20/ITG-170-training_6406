class Employee:
    def __init__(self, name, address, salary, job_title):
        self.name = name
        self.address = address
        self.salary = salary
        self.job_title = job_title

    def calculate_bonus(self):
        raise NotImplementedError

    def performance_report(self):
        raise NotImplementedError

    def manage_projects(self):
        raise NotImplementedError

    def get_details(self):
        return f"{self.name} ({self.job_title}) - {self.address}, salary={self.salary:.2f}"


class Manager(Employee):
    def calculate_bonus(self):
        return f"{self.name} bonus: {self.salary * 0.20:.2f}"

    def performance_report(self):
        return f"{self.name} performs well by coordinating teams and delivering goals."

    def manage_projects(self):
        return f"{self.name} manages multiple projects across the department."


class Developer(Employee):
    def calculate_bonus(self):
        return f"{self.name} bonus: {self.salary * 0.15:.2f}"

    def performance_report(self):
        return f"{self.name} delivers clean code and meets sprint deadlines."

    def manage_projects(self):
        return f"{self.name} supports project development and code reviews."


class Programmer(Employee):
    def calculate_bonus(self):
        return f"{self.name} bonus: {self.salary * 0.12:.2f}"

    def performance_report(self):
        return f"{self.name} writes reusable code and fixes bugs efficiently."

    def manage_projects(self):
        return f"{self.name} assists with project tasks and implements features."

manager = Manager("Alice", "123 Park Ave", 120000, "Manager")
developer = Developer("Bob", "234 Tech Blvd", 95000, "Developer")
programmer = Programmer("Charlie", "345 Code St", 90000, "Programmer")

print(manager.get_details())
print(manager.performance_report())
print(manager.calculate_bonus())
print(manager.manage_projects())

print(developer.get_details())
print(developer.performance_report())
print(developer.calculate_bonus())
print(developer.manage_projects())

print(programmer.get_details())
print(programmer.performance_report())
print(programmer.calculate_bonus())
print(programmer.manage_projects())
