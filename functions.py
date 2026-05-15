def greet():
    print("im geetha saying hello to you")
greet()
##second function
def Max(a,b):
    return max(a,b)
print(Max(99,87))
#third function
length=int(input("Enter length: "))
breadth=int(input("Enter breadth: "))
def rectangle_area(length,breadth):
    return 2*(length+breadth)
print(rectangle_area(length,breadth))
##sum of n numbers
n=int(input())
def adding(n):
    sum=0
    for i in range(n):
        sum += i
    return sum
print(adding(n))