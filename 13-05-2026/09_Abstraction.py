from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("The animal is sleeping.")


class Dog(Animal):
    def sound(self):
        print("Dog barks: Woof! Woof!")


# Test
animal = Dog()
animal.sound()
animal.sleep()
