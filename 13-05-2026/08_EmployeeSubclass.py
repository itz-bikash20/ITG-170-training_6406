class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

class Employee(Person):
    def __init__(self, first_name, last_name, job_title, employee_id):
        super().__init__(first_name, last_name)
        self.job_title = job_title
        self.employee_id = employee_id

    def get_employee_id(self):
        return self.employee_id

    def get_last_name(self):
        return f"{super().get_last_name()} ({self.job_title})"

employee = Employee("Praveen", "Kumar", "Developer", 1001)
print(employee.get_first_name())
print(employee.get_last_name())
print("Employee ID:", employee.get_employee_id())
