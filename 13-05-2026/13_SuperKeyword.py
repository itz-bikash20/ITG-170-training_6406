class Animal:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Animal name: {self.name}")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def display_info(self):
        super().display_info()
        print(f"Breed: {self.breed}")


dog = Dog("Buddy", "Labrador")
dog.display_info()
