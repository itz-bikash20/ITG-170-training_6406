import math_utils
print(math_utils.add(5,10))
# Check if any number in the list is negative
numbers = [1, 2, 3, 4, 5]
has_negative = any(num >  0 for num in numbers)
print("Contains negative number:", has_negative)

# Check if all numbers are positive
all_positive = all(num > 0 for num in numbers)
print("All numbers are positive:", all_positive)

# Generator that prints numbers from 1 to 5
def number_generator():
    for i in range(1, 6):
        yield i

for num in number_generator():
    print(num)

# Use with statement to open a file and print its contents
with open('/home/miracle/python_workspace/example.txt', 'r') as file:
    contents = file.read()
    print(contents)

# Module for simple interest
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

# Import and use the function
simple_interest = calculate_simple_interest(1000, 5, 2)
print("Simple Interest:", simple_interest)

# Iterator for a list of numbers
class NumberIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.numbers):
            result = self.numbers[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

numbers_list = [10, 20, 30]
for number in NumberIterator(numbers_list):
    print(number)

# Generator that yields even numbers up to 10
def even_number_generator():
    for i in range(0, 11, 2):
        yield i

for even in even_number_generator():
    print(even)

# Check if a list contains a number greater than 100
large_numbers = [10, 20, 30, 150]
contains_large = any(num > 100 for num in large_numbers)
print("Contains number greater than 100:", contains_large)
