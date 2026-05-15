def greet():
    """Prints a welcome message to the user."""
    print("Welcome to the ATM System!")


def max_number(a, b):
    """Returns the larger of two numbers."""
    return max(a, b)


def rectangle_area(length, width):
    return length * width


def sum_numbers(*numbers):
    """Calculates the sum of any number of numbers passed as arguments."""
    return sum(numbers)


def square(n):
    return n ** 2


def is_even(n):
    return n % 2 == 0


def greet_user(name):
    print(f"Hello, {name}! Welcome to the ATM.")


def average_three(a, b, c):
    return (a + b + c) / 3


# Test the functions
if __name__ == "__main__":
    greet()
    print(f"Max of 5 and 10: {max_number(5, 10)}")
    print(f"Rectangle area: {rectangle_area(4, 5)}")
    print(f"Sum: {sum_numbers(1, 2, 3, 4, 5)}")
    print(f"Square of 7: {square(7)}")
    print(f"Is 4 even? {is_even(4)}")
    greet_user("geetha")
    print(f"Average of 10, 20, 30: {average_three(10, 20, 30)}")