# Assignment Tasks
# Create a module named math_utils.py with a function to add two numbers. Import and use it.
import math_utils
result = math_utils.add(5, 10)
print("The sum is:", result)

# Write a program using any() to check if any number in a list is negative.
nums = [1, 2, -3, 4, 5]
has_negative = any(n < 0 for n in nums)
print(has_negative)

# Write a program using all() to check if all numbers are positive.
nums = [1, 2, 3, 4, 5]
all_positive = all(n > 0 for n in nums)
print(all_positive)

# Create a generator that prints numbers from 1 to 5.
def number_generator():
    for i in range(1, 6):
        yield i

for number in number_generator():
    print(number)

# Use with statement to open a file and print its contents.

with open("example.txt", "a+") as file:
    file.write("Hello, World!\n")
    file.seek(0)
    contents = file.read()
    print(contents)


# Create a module that contains a function to calculate simple interest.

from math_utils import simple_interest
interest = simple_interest(1000, 5, 2)
print("Simple Interest:", interest)


# Import the module and use the function.
# Create an iterator for a list of numbers.
nums = [1, 2, 3, 4, 5]
num_iter = iter(nums)
print(next(num_iter))
print(next(num_iter))

# Write a generator that yields even numbers up to 10.
def even_generator():
    for i in range(0, 11, 2):
        yield i
# Use any() to check if a list contains a number greater than 100.
nums = [1, 2, 3, 4, 5]
has_large_number = any(n > 100 for n in nums)
print(has_large_number)
