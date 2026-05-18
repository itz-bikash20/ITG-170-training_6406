class StaticKeyword:
    employee_count = 0

    def __init__(self, name):
        self.name = name
        StaticKeyword.employee_count += 1

    @staticmethod
    def get_employee_count():
        return StaticKeyword.employee_count

    def show_name(self):
        print("Employee Name:", self.name)


first = StaticKeyword("Alice")
second = StaticKeyword("Bob")

first.show_name()
second.show_name()
print("Total employees:", StaticKeyword.get_employee_count())
