class ThisKeyword:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


example = ThisKeyword("Praveen", 28)
example.print_details()
