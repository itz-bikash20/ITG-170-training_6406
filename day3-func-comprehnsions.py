# 1. Function to print welcome message

def greet():
    print("Welcome to Python Programming")

greet()


# 2. Function to return larger number

def larger(a, b):
    if a > b:
        return a
    else:
        return b

print("Larger number is:", larger(10, 20))


# 3. Function to calculate area of rectangle

def area_rectangle(length, breadth):
    return length * breadth

print("Area of Rectangle:", area_rectangle(5, 4))


# 4. Function to accept any number of values and return sum

def total_sum(*numbers):
    return sum(numbers)

print("Sum:", total_sum(10, 20, 30, 40))


# 5. Function with doc string

def square(num):
    """
    This function returns the square of a number.
    """
    return num * num

print("Square:", square(6))


# 6. Function to return square of a number

def square_number(n):
    return n ** 2

print("Square is:", square_number(8))


# 7. Function to check even number

def is_even(num):
    if num % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"

print(is_even(12))


# 8. Function to greet user using name

def greet_user(name):
    print("Hello", name)

greet_user("Dora")


# 9. Function to find average of 3 numbers

def average(a, b, c):
    return (a + b + c) / 3

print("Average is:", average(10, 20, 30))


# 10. Proper doc string example

def addition(a, b):
    """
    This function takes two numbers as input
    and returns their addition.
    """
    return a + b

print("Addition:", addition(5, 7))




#COMPEHENSIONS
# 1. Create a list of 5 fruits and print first and last fruit

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print("First Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])


# 2. Create a list of numbers from 1–10 using list comprehension

numbers = [i for i in range(1, 11)]

print("Numbers:", numbers)


# 3. Filter numbers greater than 5

nums = [2, 5, 7, 1, 9, 3, 10]

filtered = [i for i in nums if i > 5]

print("Numbers greater than 5:", filtered)


# 4. Create a dictionary storing Name, Age, Course

student = {
    "Name": "Dora",
    "Age": 21,
    "Course": "Python"
}

print("Keys:", student.keys())
print("Values:", student.values())


# 5. Dictionary comprehension for squares from 1–5

squares = {i: i**2 for i in range(1, 6)}

print("Squares Dictionary:", squares)


# 6. Create a list of 5 favorite movies and print using loop

movies = ["Bahubali", "RRR", "Kalki", "Pushpa", "Salaar"]

print("Favorite Movies:")

for movie in movies:
    print(movie)


# 7. Add a new movie and remove one movie

movies.append("Devara")

movies.remove("RRR")

print("Updated Movies List:", movies)


# 8. Product dictionary and total cost calculation

product = {
    "name": "Laptop",
    "price": 50000,
    "quantity": 2
}

total_cost = product["price"] * product["quantity"]

print("Total Cost:", total_cost)


# 9. List comprehension for odd numbers from 1–20

odd_numbers = [i for i in range(1, 21) if i % 2 != 0]

print("Odd Numbers:", odd_numbers)


# 10. Filter names longer than 4 letters

names = ["Ram", "Suresh", "Dora", "Pravallika", "John"]

long_names = [name for name in names if len(name) > 4]

print("Names longer than 4 letters:", long_names)