# 1. Try-Except Block
print("1. Try-Except Block")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter valid numbers")

print()

# 2. Multiple Except Blocks
print("2. Multiple Except Blocks")
try:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))

    print("Division:", a / b)

except ZeroDivisionError:
    print("Division by zero is not allowed")

except ValueError:
    print("Only integers are allowed")

except Exception as e:
    print("Some other error occurred:", e)

print()


# 3. Nested Try
print("3. Nested Try")

try:
    num = int(input("Enter a number: "))

    try:
        result = 100 / num
        print("Result:", result)

    except ZeroDivisionError:
        print("Cannot divide by zero")

except ValueError:
    print("Invalid input")

print()


# 4. Finally Block
print("4. Finally Block")

try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program execution completed")

print()


# 5. Raise Keyword
print("5. Raise Keyword")

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise Exception("You are not eligible to vote")

    else:
        print("You are eligible to vote")

except Exception as e:
    print("Error:", e)

print()


# 6. Throws Concept Equivalent -- In Python, there is no exact throws keyword like Java.
#But we can create a function that may raise an exception.
print("6. Throws Concept Equivalent")

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    return x / y

try:
    result = divide(10, 0)
    print("Result:", result)
except ZeroDivisionError as e:
    print("Error:", e)