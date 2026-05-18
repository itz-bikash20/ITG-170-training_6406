# Program to Show Overloading of Methods in Class

class Area:
    def area(self, a,b):
        pass
class Square(Area):
    def area(slef,a):
        return f"Area of Square is {a*a}"
class Rectangle(Area):
    def area(self,a,b):
        return f"Area of Rectangle is {a*b}"
s = Square()
print(s.area(5))
r = Rectangle()
print(r.area(5,10))