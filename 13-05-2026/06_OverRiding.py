class Animal:
    def sound(self):
        return "Animal makes a sound"
class Dog(Animal):
    def sound(self):
        return "Dog barks"

class Cat(Animal):
    def sound(self):
        return "Cat meows"

c = Cat()
print(c.sound())
d = Dog()
print(d.sound())
