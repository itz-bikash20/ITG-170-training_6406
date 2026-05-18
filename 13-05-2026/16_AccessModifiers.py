class Person:
    def __init__(self, name, age, department):
        self.name = name   
        self._age = age           
        self.__department = department  

    def get_name(self):
        return self.name

    def get_age(self):
        return self._age

    def get_department(self):
        return self.__department

    def print_details(self):
        print(f"Person details: {self.name}, age {self._age}, department {self.__department}")


class EmployeeHelper:
    def show_protected_age(self, person):
        print("Protected age access:", person._age)


person = Person("Praveen", 30, "IT")
print("Name:", person.get_name())
print("Age:", person.get_age())
print("Department:", person.get_department())
person.print_details()

helper = EmployeeHelper()
helper.show_protected_age(person)
