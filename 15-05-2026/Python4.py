# Assignment Tasks
# Create a function greet() that prints a welcome message.
def greet():
    print("Welcome to the Python programming course!")
greet()

# Create a function that accepts two numbers and returns the larger number.
def larger(a, b):
    if a > b:
        return a
    else:
        return b
print(larger(10, 20))

# Write a function that calculates the area of a rectangle.

def area(length, width):
    return length * width
print(area(5, 3))


# Create a function that accepts any number of numbers and returns their sum.

def sum_numbers(*args):
    return sum(args)
print(sum_numbers(1, 2, 3, 4, 5))

# Add a doc string to any one function explaining what it does.

def sum_numbers(*args):
    """This function accepts any number of numbers and returns their sum."""
    return sum(args)
print(sum_numbers(1, 2, 3, 4, 5))


# Write a function that returns the square of a number.
def square(n):
    """This function returns the square of a number."""
    return n ** 2

print(square(5))

# Write a function that checks if a number is even.
def is_even(n):
    """This function checks if a number is even."""
    return n % 2 == 0

print(is_even(4)) 
print(is_even(7))

# Create a function that greets a user using their name (parameter).
def greet_user(name):
    """This function greets a user using their name."""
    print(f"Hello, {name}!")

greet_user("Alice")


# Create a function that finds the average of 3 numbers.
def average_of_three(a, b, c):
    """This function finds the average of 3 numbers."""
    return (a + b + c) / 3

print(average_of_three(10, 20, 30))

# Add proper doc string to one function
