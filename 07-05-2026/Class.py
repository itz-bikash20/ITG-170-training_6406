class Parent:
    def height(height):
        print(height)

    def color(self,color):
        print(color)

class Child(Parent):
    def age(slef,age):
        print(age)
    
c = Child()

c.color(input("Enter color"))
c.height(int(input("enter height")))
c.age(int(input("enter age")))